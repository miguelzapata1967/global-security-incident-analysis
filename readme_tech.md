The project demonstrates an end-to-end data analytics and engineering workflow using **Python, Snowflake, dbt, Git/GitHub, and Power BI**.

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