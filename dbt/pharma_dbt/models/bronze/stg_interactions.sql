/*
Model: STG_INTERACTIONS

Purpose:
Standardize sales representative interaction records.

Source:
PHARMA_DB.BRONZE.INTERACTIONS

Materialization:
View
*/

select
    interaction_id,
    account_id,
    rep_id,
    interaction_date,
    interaction_type
from {{ source('bronze', 'INTERACTIONS') }}