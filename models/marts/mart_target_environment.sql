{{ config(materialized = 'table') }}
with incidents as (

    select *
    from {{ ref('int_gtd_incidents') }}

)
select
    TARGET_ENVIRONMENT,
    count(*) as incident_count
from incidents
group by TARGET_ENVIRONMENT