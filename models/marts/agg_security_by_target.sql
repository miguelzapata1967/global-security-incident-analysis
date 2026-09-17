select

    target_environment,
    severity_category,

    count(*) as incidents,
    sum(total_casualties) as total_casualties,
    sum(nkill) as fatalities,
    sum(nwound) as wounded

from {{ ref('fct_security_incidents') }}

group by
    target_environment,
    severity_category