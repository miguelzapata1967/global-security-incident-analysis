# Mass Shooting Incident Severity and Physical Security Analysis



## Technical Documentation



This document describes the technical implementation of the Global and Domestic Violent Events analysis project.



The project was designed as an end-to-end analytics workflow:



```text

Raw Source Data

&#x20;      ↓

Python / Pandas

&#x20;      ↓

Data Inspection & Validation

&#x20;      ↓

Data Cleaning & Transformation

&#x20;      ↓

Analytical CSV Files

&#x20;      ↓

AWS S3

&#x20;      ↓

Snowflake RAW Layer

&#x20;      ↓

dbt

&#x20;      ↓

Staging & Fact Models

&#x20;      ↓

Power BI

&#x20;      ↓

Interactive Analysis

```



The analytical findings and interpretation are documented separately in:



[readme_analysis.md](readme_analysis.md)



---



# 1. Technology Stack



The project uses:



- Python

- Pandas

- CSV / Excel

- AWS S3

- Snowflake

- SQL

- dbt

- Power BI

- Git

- GitHub



Each technology performs a specific part of the analytical workflow.



---



# 2. Source Data



The project uses violent-event and mass-shooting datasets containing information such as:



- incident date;

- country;

- geographic location;

- latitude and longitude;

- attack type;

- target type;

- weapon type;

- firearm subtype;

- fatalities;

- injuries;

- incident characteristics.



The raw source files were preserved separately from the transformed analytical datasets.



This allows the transformation process to remain traceable and reproducible.



---



# 3. Initial Data Inspection



The first stage of the project used Python and Pandas to inspect the datasets before performing transformations.



Primary inspection script:



`python_01_inspect_data.py`



The inspection process examined:



- dataset dimensions;

- column names;

- data types;

- missing values;

- potential duplicates;

- geographic fields;

- attack categories;

- target categories;

- weapon categories;

- casualty fields.



The objective was to understand the structure and limitations of the data before modifying it.



---



# 4. Python Analytical Dataset Creation



The script:



`01_create_analytical_dataset.py`



was used to create the primary analytical dataset.



Python and Pandas were used to select and transform fields needed for downstream analysis.



The transformation process focused on retaining fields relevant to:



- firearm incidents;

- casualty analysis;

- physical-security targets;

- geographic analysis;

- attack classification;

- weapon classification.



The resulting analytical dataset could then be validated independently from the original source data.



---



# 5. Data Quality Validation



Data quality was examined using:



`02_gtd_data_quality.py`



Additional validation was performed using:



`02_validate_firearm_dataset.py`



The validation process examined issues such as:



- null values;

- missing geographic coordinates;

- casualty fields;

- firearm classifications;

- unexpected values;

- analytical record counts;

- possible duplicate records.



The purpose of validation was not to automatically modify questionable records.



Instead, records were evaluated before determining whether they should be transformed, retained, excluded from a specific analysis, or documented as a limitation.



---



# 6. Analytical Scope



The script:



`03_gtd_analytical_scope.py`



was used to define the analytical scope of the project.



The analysis progressively narrowed the source data into subsets relevant to the research questions.



One of the primary subsets contained:



**1,718 firearm-related incidents**



A security-relevant analytical filter subsequently identified:



**1,629 security-relevant firearm incidents**



The filtering logic allowed the project to focus on target environments relevant to physical-security analysis while preserving the original source information.



---



# 7. Data Cleaning



The script:



`04_gtd_clean_data.py`



performed cleaning and transformation operations required for downstream analysis.



The resulting cleaned dataset is stored as:



`gtd_cleaned.csv`



Supporting analytical datasets include:



`gtd_analytical_scope.csv`



`firearm_security_incidents.csv`



`gtd_data_quality_report.csv`



These files provide intermediate and final analytical outputs generated during the Python portion of the project.



---



# 8. Geographic Data Quality



Latitude and longitude were important fields because the final Power BI dashboard includes geographic visualization.



During validation, **39 records were identified with missing latitude and/or longitude information**.



These records were not automatically deleted.



They represent documented incidents that may remain valid for:



- incident counts;

- casualty analysis;

- attack-type analysis;

- target analysis;

- weapon analysis.



However, records without usable coordinates cannot be reliably plotted as individual geographic points.



Therefore, the technical workflow separates:



```text

Valid incident record

```



from:



```text

Record suitable for geographic visualization

```



This prevents map requirements from changing the underlying incident totals.



---



# 9. AWS S3 Staging



After Python preprocessing, the analytical data was prepared for cloud ingestion.



AWS S3 was used as the staging layer.



The project used an S3 path structured around:



`/raw/gtd/`



This provides a separation between locally processed data and the Snowflake data warehouse.



The general flow was:



```text

Python

&#x20;  ↓

CSV

&#x20;  ↓

AWS S3

&#x20;  ↓

Snowflake

```



---



# 10. Snowflake Data Warehouse



Snowflake was used as the cloud data warehouse.



Primary database:



`GTD_SECURITY`



The project used a RAW layer for ingested data and a separate schema for dbt-generated analytical objects.



Schemas included:



`RAW`



and



`dbt_mzapata`



The Snowflake warehouse used during development was:



`COMPUTE_WH`



---



# 11. Snowflake RAW Layer



Source data was loaded into Snowflake before dbt transformations were applied.



One of the primary analytical files loaded was:



`firearm_security_incidents.csv`



The loaded firearm analytical dataset contained:



**1,718 records**



The RAW layer preserves the ingested data before downstream dbt transformations.



---



# 12. Snowflake File Format



CSV ingestion required a Snowflake file format.



The loading configuration included handling for differences in source-column structure.



One relevant configuration was:



```sql

ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE

```



This allowed ingestion to account for source-file structural differences while the data was subsequently validated and transformed.



This setting should not be interpreted as ignoring data-quality problems. Validation remained part of the analytical process.



---



# 13. dbt Transformation Layer



dbt was used to transform the Snowflake RAW data into reusable analytical models.



The local dbt project was configured with:



`my_snowflake_project`



The dbt target schema was:



`dbt_mzapata`



dbt was used to separate staging logic from final analytical models.



---



# 14. dbt Sources



Primary dbt sources included:



`gtd_raw`



and



`firearm_security_incidents`



These sources provided the starting point for downstream staging and fact models.



---



# 15. dbt Staging Models



The project created staging views including:



`stg_gtd_events`



`stg_gtd_attacks`



`stg_gtd_casualties`



`stg_gtd_security`



The staging layer provides cleaned and standardized representations of the source data.



This design prevents Power BI from depending directly on raw ingestion tables.



---



# 16. dbt Fact Models



Final analytical models included:



`fct_gtd_incidents`



and



`fct_security_incidents`



These models support the primary analytical questions and Power BI reporting.



The transformation architecture therefore follows:



```text

RAW

&#x20;↓

STAGING

&#x20;↓

FACT

&#x20;↓

POWER BI

```



---



# 17. dbt Materialization



Staging models were materialized primarily as views.



This allowed transformations to remain logically separated while avoiding unnecessary duplication of data during development.



The dbt project successfully completed:



```text

dbt parse

dbt compile

dbt run

```



during project development.



---



# 18. Severity Transformation



A severity classification was created to make casualty impact easier to analyze.



The final Snowflake analytical model produced:



| Severity | Records |

|---|---:|

| Critical | 183 |

| High | 201 |

| Low | 986 |

| No Casualties | 348 |

| **Total** | **1,718** |



The classification became an analytical dimension available to Power BI.



This severity system is specific to this portfolio analysis and is not presented as an official government classification.



---



# 19. Data Validation Between Layers



Record counts were checked throughout the pipeline.



For example, the firearm dataset contained:



**1,718 records**



and the final severity classification also totaled:



**1,718 records**



This type of reconciliation helps verify that transformation logic did not unintentionally remove or duplicate incidents.



Validation between pipeline stages is an important part of the project because a successful SQL query or dbt run does not independently prove that the resulting analytical data is correct.



---



# 20. Power BI



Power BI was used as the final visualization and reporting layer.



The primary dashboard file is:



`Domestic and Global violent events.pbix`



A PDF version is also included:



`Domestic and Global violent events.pdf`



The dashboard includes analysis of:



- global violent incidents;

- domestic violent incidents;

- geographic distribution;

- target categories;

- security-relevant incidents;

- weapons;

- attack methods;

- severity;

- summary trends.



---



# 21. Dashboard Images



GitHub-compatible images were exported so recruiters and reviewers can see dashboard results without requiring Power BI Desktop.



Included images are:



`global-violent-events-map.png`



`domestic-violent-events-map.png`



`security-by-country.png`



`security-by-target.png`



`weapons-attack-methods.png`



`summary-trends.png`



These images are displayed directly from the main `README.md`.



---



# 22. Project File Structure



The local project contains the following major components:



```text

Active_Shooter_Global_Terrorism/

│

├── README.md

├── readme_analysis.md

├── readme_tech.md

├── .gitignore

│

├── python_01_inspect_data.py

├── 01_create_analytical_dataset.py

├── 02_gtd_data_quality.py

├── 02_validate_firearm_dataset.py

├── 03_gtd_analytical_scope.py

├── 04_gtd_clean_data.py

│

├── firearm_security_incidents.csv

├── gtd_analytical_scope.csv

├── gtd_cleaned.csv

├── gtd_data_quality_report.csv

│

├── Domestic and Global violent events.pbix

├── Domestic and Global violent events.pdf

│

├── global-violent-events-map.png

├── domestic-violent-events-map.png

├── security-by-country.png

├── security-by-target.png

├── weapons-attack-methods.png

└── summary-trends.png

```



---



# 23. Git Security



The repository uses a `.gitignore` file to prevent common sensitive or unnecessary files from being committed.



Examples include:



```text

.env

*.pem

*.key

__pycache__/

.venv/

target/

dbt_packages/

logs/

```



Credentials and private authentication keys should never be committed to the repository.



---



# 24. Reproducibility



The project documents the transformation process through Python scripts, intermediate analytical files, SQL/dbt transformations, and final visualization outputs.



The purpose is to make the analytical process traceable:



```text

Source

&#x20;  ↓

Inspect

&#x20;  ↓

Validate

&#x20;  ↓

Clean

&#x20;  ↓

Transform

&#x20;  ↓

Load

&#x20;  ↓

Model

&#x20;  ↓

Validate Again

&#x20;  ↓

Visualize

&#x20;  ↓

Interpret

```



This is important because the final dashboard represents only the last stage of the analytical process.



The underlying validation and transformation decisions determine whether the dashboard can be trusted.



---



# 25. Technical Lessons



Several technical lessons emerged from the project.



### Validate Before Transforming



Understanding the source data before cleaning reduces the risk of changing legitimate records.



### Preserve Raw Data



Maintaining a RAW layer makes it possible to trace transformed information back to its source.



### Separate Staging and Analytical Models



dbt staging and fact models create a clearer transformation architecture.



### Reconcile Record Counts



Record counts should be compared between pipeline stages to identify accidental filtering or duplication.



### Treat Nulls According to Context



A null geographic coordinate affects mapping but does not necessarily invalidate the underlying incident.



### Document Limitations



Technical limitations should be communicated to the analyst and ultimately to the people using the dashboard.



---



# Conclusion



This project demonstrates an end-to-end analytical workflow combining Python, Pandas, AWS S3, Snowflake, dbt, SQL, and Power BI.



The technical process begins with raw incident data and progresses through inspection, validation, cleaning, cloud ingestion, warehouse modeling, analytical transformation, reconciliation, and visualization.



The project was designed to demonstrate not only the ability to use analytical tools, but also the importance of validating information throughout the data pipeline.



For the detailed findings and interpretation:



## [← Analysis & Findings](readme_analysis.md)



For the main portfolio page:



## [← Project README](README.md)




