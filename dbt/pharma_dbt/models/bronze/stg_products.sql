/*
Model: STG_PRODUCTS

Purpose:
Standardize raw product data from the Bronze layer.

Source:
PHARMA_DB.BRONZE.PRODUCTS

Materialization:
View
*/

select
    product_id,
    product_name,
    brand,
    category
from {{ source('bronze', 'PRODUCTS') }}