/*
Model: STG_SALES_REP

Purpose:
Standardize sales representative master data.

Source:
PHARMA_DB.BRONZE.SALES_REP

Materialization:
View
*/

select
    rep_id,
    rep_name,
    territory
from {{ source('bronze', 'SALES_REP') }}