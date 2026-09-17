select

    severity_category,

    count(*) as incidents,
    sum(total_casualties) as total_casualties,
    sum(nkill) as fatalities,
    sum(nwound) as wounded

from {{ ref('fct_security_incidents') }}

group by
    severity_category