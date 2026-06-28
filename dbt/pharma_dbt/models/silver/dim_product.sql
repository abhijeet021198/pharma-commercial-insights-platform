/*
Model: DIM_PRODUCT

Purpose:
Create the Product Dimension from the Bronze staging layer.

Source:
STG_PRODUCTS

Materialization:
Table
*/

with products as (

    select *
    from {{ ref('stg_products') }}

)

select

    row_number() over (
        order by product_id
    ) as product_key,

    product_id,
    product_name,
    brand,
    category

from products