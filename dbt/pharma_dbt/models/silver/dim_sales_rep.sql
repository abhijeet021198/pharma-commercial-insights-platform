/*
Model: DIM_SALES_REP

Purpose:
Create the Sales Representative Dimension from the Bronze staging layer.

Source:
STG_SALES_REP

Materialization:
Table
*/

with sales_rep as (

    select *
    from {{ ref('stg_sales_rep') }}

)

select

    row_number() over (
        order by rep_id
    ) as rep_key,

    rep_id,
    rep_name,
    territory

from sales_rep