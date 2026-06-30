{{ config(
    materialized='table'
) }}

WITH

orders_summary AS (

    SELECT

        sr.territory,

        COUNT(fo.order_id) AS total_orders,

        SUM(fo.quantity) AS total_quantity,

        SUM(fo.revenue) AS total_revenue,

        MAX(fo.date_key) AS last_order_date_key

    FROM {{ ref('fact_orders') }} fo

    LEFT JOIN {{ ref('dim_sales_rep') }} sr

        ON fo.rep_key = sr.rep_key

    GROUP BY sr.territory

),

interaction_summary AS (

    SELECT

        sr.territory,

        COUNT(fi.interaction_id) AS total_interactions,

        MAX(fi.date_key) AS last_interaction_date_key

    FROM {{ ref('fact_interactions') }} fi

    LEFT JOIN {{ ref('dim_sales_rep') }} sr

        ON fi.rep_key = sr.rep_key

    GROUP BY sr.territory

),

territory_dimension AS (

    SELECT DISTINCT territory
    
    FROM {{ ref('dim_sales_rep') }}

),

territory_metrics AS (

    SELECT

        td.territory,

        COALESCE(o.total_orders, 0) AS total_orders,

        COALESCE(o.total_quantity, 0) AS total_quantity,

        COALESCE(o.total_revenue, 0) AS total_revenue,

        COALESCE(i.total_interactions, 0) AS total_interactions,

        o.last_order_date_key,

        i.last_interaction_date_key,

        ROUND(

            COALESCE(o.total_revenue, 0)

            /

            NULLIF(

                SUM(COALESCE(o.total_revenue, 0)) OVER (),

                0

            )

            * 100,

            2

        ) AS revenue_contribution_percent,

        RANK() OVER (

            ORDER BY COALESCE(o.total_revenue, 0) DESC

        ) AS revenue_rank

    FROM territory_dimension td

    LEFT JOIN orders_summary o

        ON td.territory = o.territory

    LEFT JOIN interaction_summary i

        ON td.territory = i.territory

),

final AS (

    SELECT

        tm.territory,

        tm.total_orders,

        tm.total_quantity,

        tm.total_revenue,

        tm.total_interactions,

        tm.revenue_contribution_percent,

        tm.revenue_rank,

        od.full_date AS last_order_date,

        id.full_date AS last_interaction_date

    FROM territory_metrics tm

    LEFT JOIN {{ ref('dim_date') }} od

        ON tm.last_order_date_key = od.date_key

    LEFT JOIN {{ ref('dim_date') }} id

        ON tm.last_interaction_date_key = id.date_key

)

SELECT *
FROM final