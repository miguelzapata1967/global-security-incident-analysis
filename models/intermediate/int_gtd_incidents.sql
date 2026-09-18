{{ config(materialized = 'view') }}
with stg as (

    select *
    from {{ ref('stg_gtd_raw') }}
)
select
    EVENTID,
    IYEAR,
    IMONTH,
    IDAY,
    COUNTRY_TXT,
    REGION_TXT,
    PROVSTATE,
    CITY,
    LATITUDE,
    LONGITUDE,
    COORDINATE_QUALITY,
    ATTACKTYPE1_TXT,
    TARGTYPE1_TXT,
    TARGSUBTYPE1_TXT,
    TARGET1,
    WEAPTYPE1_TXT,
    WEAPSUBTYPE1_TXT,
    WEAPDETAIL,
    SUCCESS,
    SUICIDE,
    MULTIPLE,
    NKILL,
    NWOUND,
    TOTAL_CASUALTIES,
    SEVERITY_CATEGORY,
    TARGET_ENVIRONMENT,
    GNAME,
    INDIVIDUAL,
    NPERPS,
    CLAIMED
from stg
