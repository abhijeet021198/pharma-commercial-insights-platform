/*
Model: DIM_DATE

Purpose:
Generate a reusable calendar dimension for reporting.

Materialization:
Table
*/

with dates as (

    select
        dateadd(
            day,
            row_number() over(order by seq4()) - 1,
            '2025-01-01'
        ) as full_date
    from table(generator(rowcount => 2192))

)

select

    to_number(to_char(full_date, 'YYYYMMDD')) as date_key,

    full_date,

    year(full_date) as year,

    quarter(full_date) as quarter,

    month(full_date) as month,

    monthname(full_date) as month_name,

    week(full_date) as week,

    day(full_date) as day,

    dayname(full_date) as day_name,

    case
        when dayofweekiso(full_date) in (6,7)
        then true
        else false
    end as is_weekend

from dates