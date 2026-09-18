# Mass Shooting Incident Severity and Physical Security Analysis

## Project Overview

This project analyzes security incidents using the Global Terrorism Database (GTD) to examine incident severity, casualties, target environments, geographic distribution, and physical security considerations.

The project demonstrates an end-to-end data analytics and engineering workflow using Python, Snowflake, dbt, Git/GitHub, and Power BI.

## Data Pipeline

GTD CSV Data  
↓  
Snowflake  
↓  
dbt Staging Models  
↓  
dbt Fact & Aggregate Models  
↓  
Power BI Dashboard

## Technologies Used

- **Python** — Data inspection, cleaning, transformation, and analysis
- **Snowflake** — Cloud data warehouse for storing and querying the data
- **dbt** — Data transformation, modeling, testing, and documentation
- **Power BI** — Interactive dashboard and data visualization
- **Git** — Version control
- **GitHub** — Source control and project portfolio

## Data Source

The primary dataset used in this project is the **Global Terrorism Database (GTD)**.

The current analysis uses GTD data from **January through June 2021**.

The analysis focuses on incidents involving firearms and examines characteristics relevant to incident severity and physical security, including:

- Incident location
- Attack type
- Target environment
- Fatalities
- Wounded
- Severity category
- Geographic distribution
- Monthly incident patterns

## dbt Data Models

The project uses dbt to transform the source data into analytical models.

### Staging Models

- `stg_gtd_events`
- `stg_gtd_attacks`
- `stg_gtd_casualties`
- `stg_gtd_security`

These models organize and prepare the source data for downstream analysis.

### Fact Model

- `fct_security_incidents`

The fact table provides the primary analytical dataset used for incident-level analysis.

### Aggregate Models

- `agg_security_by_severity`
- `agg_security_by_country`
- `agg_security_by_month`
- `agg_security_by_target`

These models provide summarized data for analyzing incident patterns by severity, country, month, and target environment.

### Data Quality

dbt tests were run successfully against the project models to help validate the transformed data.

## Power BI Dashboard

The Power BI dashboard provides an interactive view of the analyzed security incidents.

### Dashboard Components

- **Total Incidents** — Count of analyzed incidents
- **Total Fatalities** — Total fatalities associated with the incidents
- **Total Wounded** — Total wounded associated with the incidents
- **Incidents by Month** — Monthly incident distribution from January through June 2021
- **Incidents by Severity** — Distribution of incidents across severity categories
- **Incidents by Target Environment** — Incident counts by target environment
- **Incidents by Country** — Geographic distribution by country
- **Global Incident Distribution** — Geographic visualization of incidents worldwide
- **U.S. Incident Distribution** — Geographic visualization of incidents within the United States
- **Severity Filter** — Interactive filtering by severity category

## Key Findings

The analysis identified **1,718 firearm-related incidents** in the GTD dataset for the January–June 2021 period.

### Incident Distribution

- January: 243 incidents
- February: 231 incidents
- March: 238 incidents
- April: 321 incidents
- May: 340 incidents
- June: 345 incidents

The monthly distribution shows that the number of incidents varied across the six-month period.

### Security-Relevant Targets

The analyzed incidents involved a range of target environments, including:

- Private Citizens & Property
- Military
- Police
- Government
- Business
- Educational Institutions
- Religious Institutions
- Transportation
- Utilities

The target-environment analysis provides a way to examine where security incidents occurred and which environments may require additional physical-security consideration.

## Methodology

The project follows an ETL/ELT-style workflow:

1. **Data ingestion** — GTD data was obtained in CSV format.
2. **Data preparation** — Python was used to inspect the dataset, identify data-quality issues, and prepare the data for analysis.
3. **Data warehousing** — The prepared data was loaded into Snowflake.
4. **Transformation** — dbt was used to create staging, fact, and aggregate models.
5. **Data validation** — dbt tests were executed to validate the transformed models.
6. **Visualization** — Power BI was connected to the analytical models to create the final dashboard.

## Limitations

- The current analysis covers **January–June 2021** rather than the complete 2021 calendar year.
- The analysis is based on the available GTD records and therefore reflects the coverage and definitions of that source dataset.
- Incident classifications and target categories are dependent on the source data.
- Geographic visualizations depend on the availability and accuracy of latitude and longitude information.
- The analysis describes patterns in the available data; it does not establish causation or predict future incidents.

## Project Structure

```text
global-security-incident-analysis/
│
├── analyses/
├── logs/
├── macros/
│
├── models/
│   ├── staging/
│   │   ├── stg_gtd_events.sql
│   │   ├── stg_gtd_attacks.sql
│   │   ├── stg_gtd_casualties.sql
│   │   └── stg_gtd_security.sql
│   │
│   └── marts/
│       ├── fct_security_incidents.sql
│       ├── agg_security_by_severity.sql
│       ├── agg_security_by_country.sql
│       ├── agg_security_by_month.sql
│       └── agg_security_by_target.sql
│
├── seeds/
├── snapshots/
├── tests/
├── dbt_project.yml
├── README.md
└── .gitignore