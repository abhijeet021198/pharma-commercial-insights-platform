/*
Model: DIM_ACCOUNT

Purpose:
Create the Account Dimension from the Bronze staging layer.

Source:
STG_ACCOUNTS

Materialization:
Table
*/

with accounts as (

    select *
    from {{ ref('stg_accounts') }}

)

select

    row_number() over (
        order by account_id
    ) as account_key,

    account_id,
    account_name,
    account_type,
    city,
    state,
    region

from accounts