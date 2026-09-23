# Mass Shooting Incident Severity and Physical Security Analysis

## Project Overview

This portfolio project analyzes firearm-related security incidents using the **Global Terrorism Database (GTD)** for **January–June 2021**.

The analysis focuses on incident frequency, severity, casualties, target environments, countries, weapons, and attack methods from a physical-security perspective.


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
GitHub: https://github.com/miguelzapata1967  "...DOCS \ "Domestic and Global violent events.pdf"

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


### Handling Null and Missing Data

Null and missing values were reviewed during the initial data-profiling process.

Not all null values represent data-quality errors. In incident datasets, a field may be blank because the information was **not reported, not applicable, or not available in the source data**.

The analysis therefore distinguishes between:

- Missing information that is expected within the source dataset
- Fields that are required for the analytical model
- Values that could affect calculations or classifications

Null-value checks were performed before transformation so that missing information could be identified and handled appropriately without automatically treating every null as an error.

This is an important part of the data-quality process because **clean data does not necessarily mean removing every null value**. The goal is to understand what the missing value represents and determine whether it affects the analysis.

### Geographic Data Limitations and Missing Coordinates

During the data-quality review of the Global Terrorism Database (GTD), **35 incident records were identified with missing latitude and/or longitude values**. These records remain valid incident records and were **not removed from the analytical dataset simply because geographic coordinates were unavailable**. The missing coordinates represent a limitation in the source data rather than evidence that the incidents did not occur or that the records were invalid. Because latitude and longitude are required to plot an incident on a geographic map, these 35 records cannot be accurately displayed as individual locations in the Power BI map visual. However, they remain available for other analyses, including incident counts, severity, casualties, target characteristics, and other non-geographic dimensions. This distinction is important because excluding these incidents solely for visualization could understate the overall number of incidents and potentially bias other analytical results. Therefore, the project preserves these records in the dataset while treating their geographic fields as missing and documenting the limitation. Geographic visualizations should consequently be interpreted as representing **only incidents with usable geographic coordinates**, rather than the complete population of incidents in the dataset.

### Separation of Analytical and Technical Documentation

This document focuses on the analytical interpretation and security perspective of the project—what the data represents, what can be concluded from the available information, and how limitations affect the interpretation of the results. 
The technical implementation, including data profiling, NULL and missing-value handling, transformations, dbt models, data-quality testing, Snowflake processing, and the Python-to-Snowflake-to-dbt-to-Power BI workflow, is documented separately in README_TECH.md.