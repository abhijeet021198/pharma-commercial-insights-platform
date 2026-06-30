{{ config(
    materialized='table'
) }}

WITH

orders_summary AS (
    SELECT

        account_key,

        COUNT(order_id) AS total_orders,

        SUM(quantity) AS total_quantity,

        SUM(revenue) AS total_revenue,

        MAX(date_key) AS last_order_date_key

    FROM {{ ref('fact_orders') }}

    GROUP BY account_key
),

interaction_summary AS (
    SELECT

        account_key,

        COUNT(interaction_id) AS total_interactions,

        MAX(date_key) AS last_interaction_date_key

    FROM {{ ref('fact_interactions') }}

    GROUP BY account_key
),

account_dimension AS (
    SELECT

        account_key,

        account_id,

        account_name,

        account_type,

        city,

        state,

        region

    FROM {{ ref('dim_account') }}

),

account_metrics AS (
    SELECT

        o.account_key,

        o.total_orders,

        o.total_quantity,

        o.total_revenue,

        ROUND(
            o.total_revenue / NULLIF(o.total_orders, 0),
            2
        ) AS avg_revenue_per_order,

        o.last_order_date_key,

        COALESCE(i.total_interactions, 0) AS total_interactions,

        i.last_interaction_date_key

    FROM orders_summary o

    LEFT JOIN interaction_summary i

        ON o.account_key = i.account_key

),

final AS (

    SELECT

        d.account_key,

        d.account_id,

        d.account_name,

        d.account_type,

        d.city,

        d.state,

        d.region,

        m.total_orders,

        m.total_quantity,

        m.total_revenue,

        m.avg_revenue_per_order,

        m.total_interactions,

        od.full_date AS last_order_date,

        id.full_date AS last_interaction_date

    FROM account_dimension d

    LEFT JOIN account_metrics m

        ON d.account_key = m.account_key

    LEFT JOIN {{ ref('dim_date') }} od

        ON m.last_order_date_key = od.date_key

    LEFT JOIN {{ ref('dim_date') }} id

        ON m.last_interaction_date_key = id.date_key

)

SELECT *
FROM final