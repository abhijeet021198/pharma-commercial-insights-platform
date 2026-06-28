/*
Model: FACT_ORDERS

Purpose:
Create the Order Fact table by linking transactional order data
to warehouse dimensions.

Materialization:
Table
*/

with orders as (

    select *
    from {{ ref('stg_orders') }}

),

fact_orders as (

    select

        o.order_id,

        a.account_key,

        p.product_key,

        r.rep_key,

        d.date_key,

        o.quantity,

        o.revenue

    from orders o

    left join {{ ref('dim_account') }} a
        on o.account_id = a.account_id

    left join {{ ref('dim_product') }} p
        on o.product_id = p.product_id

    left join {{ ref('dim_sales_rep') }} r
        on o.rep_id = r.rep_id

    left join {{ ref('dim_date') }} d
        on o.order_date = d.full_date

)

select *
from fact_orders