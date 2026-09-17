select

    eventid,

    iyear,
    imonth,
    iday,

    country_txt,
    region_txt,
    provstate,
    city,
    latitude,
    longitude,
    specificity,
    vicinity,
    location,
    coordinate_quality,

    attacktype1_txt,

    targtype1_txt,
    targsubtype1_txt,
    target1,
    corp1,
    target_environment,

    weaptype1_txt,
    weapsubtype1_txt,
    weapdetail,

    success,
    suicide,
    multiple,

    nkill,
    nkillus,
    nwound,
    nwoundus,
    total_casualties,
    severity_category,

    gname,
    gsubname,
    individual,
    nperps,

    property,
    propextent_txt,
    propvalue,

    summary,
    motive,
    claimed

from {{ source('gtd_security', 'gtd_raw') }}