# Mass Shooting Incident Severity and Physical Security Analysis

## Project Overview

This portfolio project analyzes firearm-related security incidents using the **Global Terrorism Database (GTD)** for **January–June 2021**.

The project demonstrates an end-to-end data analytics and engineering workflow using **Python, Snowflake, dbt, Git/GitHub, and Power BI**.

The analysis focuses on incident frequency, severity, casualties, target environments, countries, weapons, and attack methods from a physical-security perspective.

---

## Storytelling and Analytical Perspective

An important part of this project is understanding the differences between the two data sources: the **Global Terrorism Database (GTD)** and the **FBI mass-shooting dataset**.

The GTD is a global terrorism and security database that includes incidents occurring in the United States, while the FBI dataset focuses specifically on mass-shooting incidents in the United States.

One observation from comparing the sources is that the GTD contains more U.S. incidents within the available data than the FBI dataset. **This comparison is not intended to determine that one database is better than the other.** Instead, it highlights the importance of understanding how different datasets define and collect information.

The two sources provide different perspectives because they may differ in:

- Incident definitions
- Time coverage
- Inclusion criteria
- Target types
- Attack methods
- Weapon classifications
- Casualty measurements
- Geographic coverage
- Incident categorization

Both datasets contain **overlapping categories of information**, such as incident dates, locations, targets, weapons, and casualties. However, the definitions and collection methodologies can differ. Understanding these differences is important before comparing or combining the data.

For this phase of the project, the GTD provides a broader dataset with worldwide coverage, even though the available file currently covers only **January through June 2021**. The FBI dataset provides an additional U.S.-focused perspective for comparison.

### From Incident Investigation to Data Analysis

My background in **law enforcement and physical security** has taught me to look beyond the initial incident report and ask:

- What happened?
- Where did it happen?
- Who or what was affected?
- How severe was the incident?
- What factors contributed to the outcome?
- What patterns can be identified across incidents?

This project applies that investigative mindset to structured data.

Instead of looking at an individual incident in isolation, the analysis uses data to identify patterns in **incident severity, targets, locations, weapons, attack methods, casualties, and physical security environments**.

The analytical process follows the same basic mindset:

**Investigate → Structure the Data → Validate → Identify Patterns → Analyze → Communicate**

This approach connects my previous experience in investigations and physical security with my developing skills in **data analytics and data engineering**.

---

## Project Pipeline

**GTD CSV → Python → Snowflake → dbt → Power BI**

### 1. Data Preparation

Python was used to inspect and prepare the GTD dataset, including:

- Dataset profiling
- Data-type inspection
- Null-value checks
- Duplicate checks
- Analytical filtering
- Data preparation for warehouse processing

### 2. Data Warehouse

**Snowflake** was used as the analytical data warehouse.

- Database: `GTD_SECURITY`
- Warehouse: `COMPUTE_WH`

### 3. Data Transformation

**dbt** was used to transform the data into structured analytical models and apply data-quality tests.

### 4. Data Visualization

**Power BI** was used to create an interactive dashboard for analyzing incident trends, severity, casualties, target environments, countries, weapons, and attack methods.

---

## Technologies Used

- Python
- SQL
- Snowflake
- dbt
- Power BI
- Git
- GitHub
- ETL / ELT
- Data Modeling
- Data Quality Testing

---

## Data Sources

### Global Terrorism Database (GTD)

**Analysis period:**

**January–June 2021**

Initial dataset:

- **4,960 records**
- **135 columns**
- Approximately **17.31 MB**
- No duplicate rows identified during initial inspection

The analytical workflow focuses on firearm-related incidents within the selected GTD dataset.

### FBI Mass-Shooting Dataset

The FBI dataset provides a second, U.S.-focused perspective for the project.

It will be used to examine how a U.S.-focused mass-shooting dataset compares with the broader GTD data.

The comparison will focus on differences and similarities in areas such as:

- Incident definitions
- Time coverage
- Inclusion criteria
- Target types
- Attack methods
- Weapon classifications
- Casualties
- Geographic coverage
- Incident categorization

The two datasets will not be treated as directly interchangeable. Their definitions and collection methodologies will be examined before making comparisons or combining analytical results.

---

## dbt Models

The current dbt project contains five models:

| Model | Purpose |
|---|---|
| `stg_gtd_raw` | Prepares raw GTD data for downstream transformations |
| `int_gtd_incidents` | Creates the incident-level analytical dataset |
| `mart_security_severity` | Aggregates incidents and casualties by severity |
| `mart_severity_by_environment` | Analyzes severity across target environments |
| `mart_target_environment` | Aggregates incidents by target environment |

### Data Quality Validation

The final dbt validation produced:

- **5 / 5 models successful**
- **18 / 18 tests passed**
- **0 warnings**
- **0 errors**

Tests included validation of:

- Event ID uniqueness
- Required event IDs
- Required target environments
- Required severity categories
- Casualty fields
- Incident counts
- Average casualties
- Fatalities
- Injuries

---

## Power BI Dashboard

The completed Power BI dashboard contains four analytical pages.

### 1. Summary Trends

Provides an overview of incident activity and casualties.

Key visuals:

- Total Incidents
- Total Fatalities
- Total Wounded
- Incidents by Month
- Incidents by Severity
- Severity by Environment

### 2. Security by Target

Examines incidents by target environment.

Key visuals:

- Incidents by Target Environment
- Incidents by Severity
- Total Casualties

### 3. Security by Country

Provides country-level analysis.

Key visuals:

- Incidents by Country
- Fatalities by Country
- Selected Country — Incident Count

### 4. Weapons & Attack Methods

Examines weapons and attack methods associated with incidents.

Key visuals:

- Incidents by Weapon Type
- Incidents by Attack Type
- Casualties by Severity
- Total Wounded

---

## Key Findings

### Firearm-Related Incidents

The analysis identified:

**1,718 firearm-related incidents**

Monthly incident counts were:

| Month | Incidents |
|---|---:|
| January | 243 |
| February | 231 |
| March | 238 |
| April | 321 |
| May | 340 |
| June | 345 |
| **Total** | **1,718** |

The descriptive results show higher incident counts during the later months of the January–June period.

### Security-Relevant Incidents

The analysis identified **1,629 security-relevant firearm incidents** based on the project's target-environment classification.

Major target environments included:

| Target Environment | Incidents |
|---|---:|
| Private Citizens & Property | 628 |
| Military | 297 |
| Police | 258 |
| Government (General) | 257 |
| Business | 80 |
| Religious Figures/Institutions | 28 |
| Educational Institution | 23 |
| NGO | 18 |
| Transportation | 16 |
| Government (Diplomatic) | 14 |

These results provide a descriptive view of the types of environments represented in the dataset.

---

## Methodology

### Data Ingestion

The GTD CSV dataset was inspected and prepared for analytical processing.

### Python

Python was used for initial data profiling and preparation.

Key tasks included:

- Inspecting rows and columns
- Checking data types
- Identifying null values
- Checking duplicate records
- Preparing analytical fields

### Handling Null and Missing Data

Null and missing values were reviewed during the initial data-profiling process.

Not all null values represent data-quality errors. In incident datasets, a field may be blank because the information was **not reported, not applicable, or not available in the source data**.

The analysis therefore distinguishes between:

- Missing information that is expected within the source dataset
- Fields that are required for the analytical model
- Values that could affect calculations or classifications

Null-value checks were performed before transformation so that missing information could be identified and handled appropriately without automatically treating every null as an error.

This is an important part of the data-quality process because **clean data does not necessarily mean removing every null value**. The goal is to understand what the missing value represents and determine whether it affects the analysis.

### Snowflake

Snowflake provided the cloud data warehouse used to store and process the project data.

### dbt

dbt was used to create a repeatable transformation workflow:

**Staging → Intermediate → Mart**

This structure separates raw-data preparation, incident-level transformation, and analytical aggregation.

### Data Testing

dbt tests were executed after model creation.

Final result:

**18 tests passed successfully.**

### Power BI

Power BI was used to convert the transformed data into interactive analytical dashboards.

---

## Security Analysis Perspective

This project approaches incident data from a **physical-security and public-safety analysis perspective**.

Instead of simply counting incidents, the analysis organizes events by:

- Severity
- Casualties
- Target environment
- Country
- Weapon type
- Attack method
- Month

This demonstrates how raw incident data can be transformed into structured information for security-focused situational awareness and reporting.

---

## Limitations

Several limitations should be considered when interpreting the results:

1. **Limited time period**

   The current GTD analysis covers January–June 2021 only.

2. **Source definitions**

   GTD and FBI classifications and definitions determine how incidents, targets, weapons, casualties, and other attributes are categorized. These definitions may differ between datasets.

3. **Geographic information**

   Geographic fields may vary in completeness or precision.

4. **Descriptive analysis**

   This project describes patterns in the available data. It does not establish causation or predict future incidents.

5. **Dataset scope**

   Results reflect the records and classifications available in the selected datasets and should not be interpreted as a complete representation of all security incidents.

---

## Project Structure

```text
global-security-incident-analysis/

│
├── models/
│   ├── staging/
│   │   └── stg_gtd_raw.sql
│   │
│   ├── intermediate/
│   │   ├── int_gtd_incidents.sql
│   │   └── schema.yml
│   │
│   └── marts/
│       ├── mart_security_severity.sql
│       ├── mart_severity_by_environment.sql
│       └── mart_target_environment.sql
│
├── analyses/
├── macros/
├── seeds/
├── snapshots/
├── tests/
│
├── dbt_project.yml
├── .gitignore
└── README.md
## Skills Demonstrated

This project demonstrates practical application of:

- Python
- SQL
- Snowflake
- dbt
- Data modeling
- ETL / ELT concepts
- Data quality testing
- Data transformation
- Analytical aggregation
- Power BI
- Data visualization
- Git/GitHub
- Security-focused data analysis

---
## Power BI Dashboard

The project includes an interactive Power BI dashboard analyzing incident trends, severity, casualties, target environments, countries, weapons, and attack methods.

### Dashboard Preview

[View Power BI Dashboard PDF](docs/Dopmestic and Global violent events.pdf)

The PDF provides a static view of the Power BI analysis for portfolio and review purposes.

## Career Connection

This project connects my background in **law enforcement and private security** with my developing skills in **data analytics and data engineering**.

My previous experience involved investigations, incident response, risk awareness, problem solving, and working with information under pressure.

This project applies those analytical habits to a modern data workflow:

**Investigate → Transform → Validate → Analyze → Communicate**

The goal is to demonstrate my ability to take raw data, build a reliable analytical pipeline, validate the results, identify meaningful patterns, and communicate findings through clear visualizations.

This represents the direction of my career development:

**Investigation → Analytics → Data Engineering**

---

## Author

**Miguel Zapata**

**Data Analytics | Data Engineering | Security Data Analysis**

GitHub:

https://github.com/miguelzapata1967