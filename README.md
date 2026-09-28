# Mass Shooting Incident Severity and Physical Security Analysis



## Project Overview



This project analyzes domestic and global violent-event data to identify patterns in firearm-related incidents, casualty severity, target environments, attack methods, and geographic distribution.



The project combines my professional background in law enforcement, investigations, physical security, and threat assessment with my developing skills in data analytics and data engineering.



Rather than looking only at incident counts, the analysis focuses on questions relevant to security operations:



- Which targets experience the greatest number of firearm-related incidents?

- Which incidents produce the highest casualty levels?

- What attack methods and weapons appear most frequently?

- Which target environments show elevated security exposure?

- How are incidents geographically distributed?

- What data-quality limitations affect geographic analysis and mapping?



The project follows an end-to-end analytical workflow using Python, SQL, Snowflake, dbt, and Power BI.



---



## Analytical Workflow



```text

Source Data

   ↓

Python / Pandas

   ↓

Data Quality Validation

   ↓

Data Cleaning & Transformation

   ↓

AWS S3

   ↓

Snowflake

   ↓

dbt

   ↓

Analytical Models

   ↓

Power BI

   ↓

Security & Business Insights



Technologies Used

- Python

- Pandas

- SQL

- Snowflake

- dbt

- AWS S3

- Power BI

- Git

- GitHub

Data Sources

The project incorporates datasets related to global terrorism, mass-shooting incidents, firearm events, casualty information, attack methods, target types, and geographic information.

Source data was validated before analytical transformations were performed.

The datasets contain real-world data-quality limitations, including incomplete geographic coordinates. These limitations were documented rather than silently correcting or removing legitimate incident records.

Key Analytical Areas

The analysis examines:

- Firearm-related incidents

- Casualty severity

- Target categories

- Attack methods

- Weapon categories

- Geographic distribution

- Security-relevant environments

- Data-quality limitations

- Missing geographic coordinates

- Domestic and global violent-event patterns

Incident Severity Classification

Firearm incidents were classified into analytical severity categories based on casualty levels:

- Critical

- High

- Low

- No Casualties

This provides an additional analytical dimension beyond simply counting the number of incidents.

Dashboard Preview

Global Violent Events



Domestic Violent Events



Security Incidents by Country



Security Incidents by Target



Weapons and Attack Methods



Summary Trends



Power BI Dashboard

The interactive Power BI project file is included in this repository:

Domestic and Global violent events.pbix

A PDF export of the dashboard is also available:

Domestic and Global violent events.pdf

Data Quality

Data quality was treated as part of the analysis rather than as a separate cleanup exercise.

Some legitimate incident records contain missing or unusable latitude and longitude information. These incidents remain part of incident counts and statistical analysis when appropriate but cannot be reliably displayed on geographic Power BI maps.

This distinction is important because removing those records entirely would incorrectly reduce the number of documented incidents.

Additional details are provided in the analytical and technical documentation.

Project Documentation

The project documentation is separated into two sections to make the repository easier to review.

Analysis and Findings

See:

[readme_analysis.md](readme_analysis.md)

This document contains the detailed analytical findings, incident patterns, severity analysis, target analysis, firearm analysis, data-quality observations, limitations, and security interpretation.

Technical Implementation

See:

[readme_tech.md](readme_tech.md)

This document explains the technical workflow, including Python preprocessing, data validation, transformations, AWS S3, Snowflake, dbt modeling, and Power BI.

Python Analysis Files

The repository includes the Python scripts used throughout the project:

- python_01_inspect_data.py

- 01_create_analytical_dataset.py

- 02_gtd_data_quality.py

- 02_validate_firearm_dataset.py

- 03_gtd_analytical_scope.py

- 04_gtd_clean_data.py

These scripts document the progression from initial inspection and data-quality analysis through cleaning and creation of analytical datasets.

Purpose of the Project

The purpose of this portfolio project is not only to build a dashboard.

It demonstrates an analytical process that begins with questioning the reliability and structure of the source data, validating assumptions, identifying limitations, transforming the data, and finally communicating findings through visual analytics.

My previous experience in law enforcement, investigations, and physical security influences this approach: examine the evidence, identify inconsistencies, document limitations, and avoid drawing conclusions that the available data cannot support.

Active_Shooter_Global_Terrorism/

│

├── README.md

├── readme_analysis.md

├── readme_tech.md

│

├── Python analysis scripts

├── Analytical CSV datasets

├── Power BI dashboard

├── Dashboard PDF

├── Dashboard images

└── Data-quality documentation

Author

Miguel Angel Zapata

Security Operations & Investigations → Data Analytics

Python | SQL | Power BI | Snowflake | dbt | Data Analysis





