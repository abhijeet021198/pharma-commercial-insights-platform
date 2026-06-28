/*
Model: STG_INVENTORY

Purpose:
Standardize inventory snapshot data from the Bronze layer.

Source:
PHARMA_DB.BRONZE.INVENTORY

Materialization:
View
*/

select
    product_id,
    inventory_date,
    stock_quantity
from {{ source('bronze', 'INVENTORY') }}