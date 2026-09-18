{{ config(materialized = 'table') }}

with incidents as (

    select *
    from {{ ref('int_gtd_incidents') }}

)
select
    TARGET_ENVIRONMENT,
    count(*) as incident_count,
    sum(coalesce(NKILL, 0))  as total_fatalities,
    sum(coalesce(NWOUND, 0)) as total_injuries,
    sum(TOTAL_CASUALTIES)    as total_casualties,
    avg(TOTAL_CASUALTIES)    as avg_casualties_per_incident
from incidents
group by TARGET_ENVIRONMENT