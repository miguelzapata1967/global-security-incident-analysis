{{ config(materialized = 'table') }}

with incidents as (

    select *
    from {{ ref('int_gtd_incidents') }}

)

select
    TARGET_ENVIRONMENT,
    SEVERITY_CATEGORY,
    count(*) as incident_count
from incidents
group by
    TARGET_ENVIRONMENT,
    SEVERITY_CATEGORY