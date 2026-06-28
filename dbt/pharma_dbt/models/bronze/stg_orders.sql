/*
Model: STG_ORDERS

Purpose:
Standardize raw order transaction data from the Bronze layer.

Source:
PHARMA_DB.BRONZE.ORDERS

Materialization:
View
*/

select
    order_id,
    account_id,
    product_id,
    rep_id,
    order_date,
    quantity,
    revenue
from {{ source('bronze', 'ORDERS') }}