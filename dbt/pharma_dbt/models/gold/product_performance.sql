{{ config(
    materialized='table'
) }}

WITH

orders_summary AS (

    SELECT

        product_key,

        COUNT(order_id) AS total_orders,

        SUM(quantity) AS total_quantity_sold,

        SUM(revenue) AS total_revenue,

        MAX(date_key) AS last_order_date_key

    FROM {{ ref('fact_orders') }}

    GROUP BY product_key

),

inventory_summary AS (

    SELECT

        product_key,

        stock_quantity,

        date_key AS inventory_date_key

    FROM (

        SELECT

            product_key,

            stock_quantity,

            date_key,

            ROW_NUMBER() OVER (

                PARTITION BY product_key

                ORDER BY date_key DESC

            ) AS rn

        FROM {{ ref('fact_inventory') }}

    ) ranked_inventory

    WHERE rn = 1

),

product_dimension AS (

    SELECT

        product_key,

        product_id,

        product_name,

        brand,

        category

    FROM {{ ref('dim_product') }}

),


final AS (

    SELECT

        p.product_key,

        p.product_id,

        p.product_name,

        p.brand,

        p.category,

        COALESCE(o.total_orders, 0) AS total_orders,

        COALESCE(o.total_quantity_sold, 0) AS total_quantity_sold,

        COALESCE(o.total_revenue, 0) AS total_revenue,

        ROUND(
            COALESCE(o.total_revenue, 0) /
            NULLIF(COALESCE(o.total_orders, 0), 0),
            2
        ) AS avg_revenue_per_order,

        COALESCE(i.stock_quantity, 0) AS current_stock,

        CASE
            WHEN COALESCE(i.stock_quantity, 0) >= 5000 THEN 'High Stock'
            WHEN COALESCE(i.stock_quantity, 0) >= 3000 THEN 'Medium Stock'
            ELSE 'Low Stock'
        END AS stock_status,

        od.full_date AS last_order_date,

        id.full_date AS inventory_snapshot_date,

        RANK() OVER (
            ORDER BY COALESCE(o.total_revenue, 0) DESC
        ) AS revenue_rank

    FROM product_dimension p

    LEFT JOIN orders_summary o

        ON p.product_key = o.product_key

    LEFT JOIN inventory_summary i

        ON p.product_key = i.product_key

    LEFT JOIN {{ ref('dim_date') }} od

        ON o.last_order_date_key = od.date_key

    LEFT JOIN {{ ref('dim_date') }} id

        ON i.inventory_date_key = id.date_key

)

SELECT *
FROM final