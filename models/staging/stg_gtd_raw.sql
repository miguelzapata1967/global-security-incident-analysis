{{ config(materialized='view') }}

select *
from GTD_SECURITY.RAW.GTD_RAW
