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
    account_id,
    account_name,
    account_type,
    city,
    state,
    region
from {{ source('bronze', 'ACCOUNTS') }}