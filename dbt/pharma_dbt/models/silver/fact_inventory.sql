/*
Model: FACT_INVENTORY

Purpose:
Store daily inventory snapshots using warehouse surrogate keys.

Materialization:
Table
*/

with inventory as (

    select *
    from {{ ref('stg_inventory') }}

),

fact_inventory as (

    select

        p.product_key,

        d.date_key,

        i.stock_quantity

    from inventory i

    left join {{ ref('dim_product') }} p
        on i.product_id = p.product_id

    left join {{ ref('dim_date') }} d
        on i.inventory_date = d.full_date

)

select *
from fact_inventory