/*
Model: FACT_INTERACTIONS

Purpose:
Store customer interaction events using warehouse surrogate keys.

Materialization:
Table
*/

with interactions as (

    select *
    from {{ ref('stg_interactions') }}

),

fact_interactions as (

    select

        i.interaction_id,

        a.account_key,

        r.rep_key,

        d.date_key,

        i.interaction_type

    from interactions i

    left join {{ ref('dim_account') }} a
        on i.account_id = a.account_id

    left join {{ ref('dim_sales_rep') }} r
        on i.rep_id = r.rep_id

    left join {{ ref('dim_date') }} d
        on i.interaction_date = d.full_date

)

select *
from fact_interactions