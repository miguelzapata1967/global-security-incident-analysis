select

    eventid,

    -- Date
    iyear,
    imonth,
    iday,

    -- Location
    country_txt,
    region_txt,
    provstate,
    city,
    latitude,
    longitude,
    coordinate_quality,

    -- Attack
    attacktype1_txt,
    success,
    suicide,
    multiple,

    -- Target
    targtype1_txt,
    targsubtype1_txt,
    target1,
    corp1,
    target_environment,

    -- Weapon
    weaptype1_txt,
    weapsubtype1_txt,
    weapdetail,

    -- Casualties and severity
    nkill,
    nkillus,
    nwound,
    nwoundus,
    total_casualties,
    severity_category,

    -- Perpetrator
    gname,
    gsubname,
    individual,
    nperps,

    -- Property impact
    property,
    propextent_txt,
    propvalue,

    -- Context
    summary,
    motive,
    claimed

from {{ ref('stg_gtd_events') }}