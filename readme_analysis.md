# Mass Shooting Incident Severity and Physical Security Analysis



## Analytical Findings



This document contains the analytical findings from the Global and Domestic Violent Events project.



The objective was not simply to count incidents. The analysis examined firearm-related violence through a physical-security and investigative perspective, including attack type, target environment, casualty severity, weapon type, geographic distribution, and data-quality limitations.



The technical implementation is documented separately in \[`readme\_tech.md`](readme\_tech.md).



\---



## 1. Global Dataset Overview



The Global Terrorism Database (GTD) dataset analyzed for this project contained:



\*\*4,960 incidents\*\*



The analysis first examined the overall distribution of attack types, targets, and weapons before narrowing the analytical scope to firearm-related incidents.



\---



## 2. Attack Types



The most frequently recorded attack types were:



| Attack Type | Incidents |

|---|---:|

| Bombing / Explosion | 1,828 |

| Armed Assault | 1,292 |

| Unknown | 603 |

| Assassination | 450 |

| Kidnapping | 448 |

| Facility / Infrastructure Attack | 281 |

| Barricade Incident | 16 |

| Hijacking | 14 |



Bombing/explosion and armed assault represented the largest attack categories in the dataset.



However, because this project focuses heavily on mass-shooting and physical-security considerations, the analysis was subsequently narrowed to incidents involving firearms.



\---



## 3. Target Types



The most frequently recorded target categories in the complete dataset included:



| Target Type | Incidents |

|---|---:|

| Private Citizens \& Property | 1,502 |

| Military | 1,161 |

| Police | 668 |

| Government (General) | 527 |

| Business | 243 |

| Unknown | 177 |

| Terrorists / Non-State Militia | 145 |

| Utilities | 96 |

| Religious Institutions | 84 |

| Education | 75 |

| Transportation | 68 |

| Journalists \& Media | 49 |

| Diplomatic | 36 |

| Telecommunications | 33 |

| NGO | 30 |

| Violent Political Party | 25 |

| Airports | 21 |

| Maritime | 8 |

| Other | 7 |

| Food / Water Supply | 4 |

| Tourists | 1 |



Private citizens/property, military, police, and government targets represented a substantial portion of documented incidents.



\---



## 4. Weapon Categories



The weapon distribution showed:



| Weapon Type | Incidents |

|---|---:|

| Explosives | 2,089 |

| Firearms | 1,718 |

| Unknown | 775 |

| Incendiary | 259 |

| Melee | 97 |

| Vehicle | 9 |

| Sabotage Equipment | 7 |

| Chemical | 4 |

| Other | 2 |



Firearms were the second most frequently recorded weapon category, with:



\*\*1,718 firearm-related incidents\*\*



These incidents became a primary analytical subset for the project.



\---



# Firearm Incident Analysis



## 5. Firearm Incidents by Attack Type



Among the 1,718 firearm incidents:



| Attack Type | Incidents |

|---|---:|

| Armed Assault | 1,114 |

| Assassination | 276 |

| Kidnapping | 252 |

| Facility / Infrastructure Attack | 53 |

| Hijacking | 12 |

| Barricade Incident | 11 |



Armed assault represented the dominant attack type among firearm-related incidents.



\---



## 6. Firearm Incidents by Target



The firearm subset showed the following target distribution:



| Target Type | Incidents |

|---|---:|

| Private Citizens \& Property | 628 |

| Military | 297 |

| Police | 258 |

| Government (General) | 257 |

| Business | 80 |

| Terrorists / Non-State Militia | 49 |

| Religious Institutions | 28 |

| Journalists \& Media | 26 |

| Education | 23 |

| NGO | 18 |

| Transportation | 16 |

| Diplomatic | 14 |

| Violent Political Party | 11 |

| Utilities | 4 |

| Airports | 2 |

| Maritime | 2 |

| Telecommunications | 2 |

| Other | 1 |

| Tourists | 1 |

| Food / Water Supply | 1 |



The largest firearm target category was \*\*Private Citizens \& Property\*\*, followed by Military, Police, and Government targets.



This distribution demonstrates why target environment is important when analyzing violent incidents from a physical-security perspective.



\---



# Casualty Analysis



## 7. Casualties per Firearm Incident



For firearm incidents, total casualties per incident showed the following distribution:



| Statistic | Casualties |

|---|---:|

| Mean | 3.95 |

| Median | 1 |

| 75th Percentile | 4 |

| Maximum | 104 |



The difference between the mean and median indicates that the casualty distribution is influenced by a smaller number of incidents producing substantially higher casualty totals.



Therefore, incident count alone does not fully describe incident severity.



\---



## 8. Casualty Thresholds



Among the 1,718 firearm incidents:



| Threshold | Incidents |

|---|---:|

| At least 1 casualty | 1,370 |

| At least 1 death | 1,215 |

| At least 5 deaths | 284 |

| At least 10 deaths | 122 |



These thresholds demonstrate the importance of separating incident frequency from incident consequences.



An environment may experience relatively fewer incidents but still face significant security exposure if those incidents produce high casualty levels.



\---



# Severity Classification



## 9. Analytical Severity Categories



To make casualty impact easier to analyze and visualize, firearm incidents were classified into severity categories.



The final analytical model produced:



| Severity | Incidents |

|---|---:|

| Critical | 183 |

| High | 201 |

| Low | 986 |

| No Casualties | 348 |

| \*\*Total\*\* | \*\*1,718\*\* |



The categories provide a practical analytical dimension for Power BI visualization and comparison.



The classification should be understood as an \*\*analytical framework created for this project\*\*, not as an official government or law-enforcement threat classification system.



\---



## 10. High-Severity Firearm Incidents



Using a threshold of \*\*5 or more total casualties\*\*, the analysis identified:



\*\*384 high-severity firearm incidents\*\*



The target distribution was:



| Target Type | High-Severity Incidents |

|---|---:|

| Private Citizens \& Property | 154 |

| Military | 111 |

| Police | 43 |

| Government (General) | 22 |

| Business | 16 |

| Transportation | 8 |

| Diplomatic | 6 |

| NGO | 3 |

| Religious Institutions | 3 |

| Journalists \& Media | 2 |

| Airports | 1 |



Private citizens/property and military targets represented the largest groups within this high-severity subset.



\---



## 11. Weapon Subtypes in High-Severity Incidents



For the 384 high-severity firearm incidents:



| Firearm Subtype | Incidents |

|---|---:|

| Unknown Gun Type | 320 |

| Automatic / Semi-Automatic Rifle | 49 |

| Rifle / Shotgun | 9 |

| Handgun | 5 |

| Other | 1 |



A major limitation is immediately visible:



\*\*320 of the 384 high-severity incidents were recorded with an unknown gun subtype.\*\*



Therefore, the available data does not support strong conclusions about the specific firearm subtype used across most high-severity incidents.



This is an important example of why missing or incomplete data should be reported rather than replaced with assumptions.



\---



# Physical Security Analysis



## 12. Security-Relevant Firearm Incidents



The project also created a security-relevant analytical subset based on target environments considered particularly relevant to physical-security analysis.



Results:



\- \*\*1,629 security-relevant firearm incidents\*\*

\- \*\*89 firearm incidents outside the selected security-relevant scope\*\*

\- \*\*367 high-severity security-relevant incidents\*\*



This subset allows the project to move beyond general violent-event statistics and examine incidents from an operational-security perspective.



The classification represents the analytical scope of this project and should not be interpreted as an official security or government classification.



\---



# Geographic Analysis



## 13. Geographic Mapping



Latitude and longitude fields were used to visualize incidents geographically in Power BI.



The maps provide a useful method for identifying geographic concentrations and comparing incidents across locations.



However, geographic visualization introduced an important data-quality limitation.



\---



## 14. Missing Geographic Coordinates



During data validation, \*\*39 records were identified with missing latitude and/or longitude information\*\*.



These records represent legitimate incidents and therefore remain part of the appropriate incident counts and analytical totals.



However, without reliable geographic coordinates, they cannot be accurately displayed as individual points on the Power BI map.



They were therefore:



\- retained in the analytical dataset where appropriate;

\- included in incident counts and non-geographic analysis;

\- excluded from map-point visualization when coordinates were unavailable.



Removing the incidents completely would artificially reduce the number of documented events.



At the same time, inventing or estimating coordinates without sufficient supporting evidence could create false geographic precision.



The project therefore preserves the distinction between:



\*\*an incident being known to have occurred\*\*



and



\*\*the exact geographic coordinates of that incident being known.\*\*



\---



# Data Quality Findings



## 15. Data Quality as Part of the Analysis



Data cleaning was not treated as an exercise in making every field complete.



Instead, questionable and incomplete records were evaluated according to whether sufficient evidence existed to modify them.



The project followed several principles:



1\. Missing data does not automatically mean an invalid record.

2\. Repeated records should not automatically be classified as duplicates without examining the event information.

3\. Missing geographic coordinates should not be invented simply to populate a map.

4\. Unknown weapon information should remain unknown when the source data does not support a more specific classification.

5\. Analytical limitations should be communicated alongside findings.



This approach preserves the distinction between \*\*observed information, analytical interpretation, and unsupported assumptions\*\*.



\---



# Analytical Interpretation



## 16. Incident Frequency vs. Incident Severity



One of the most important analytical lessons from the project is that frequency and severity answer different questions.



Incident frequency identifies where violent events occur most often.



Severity analysis identifies where incidents produce greater human consequences.



For physical-security analysis, both dimensions matter.



A target environment with many low-casualty incidents presents a different security problem from an environment with fewer incidents but substantially higher casualty outcomes.



\---



## 17. Target Environment



Private Citizens \& Property represented the largest firearm target category in the analyzed data.



Military, police, and government targets also represented substantial portions of firearm incidents.



These findings can help frame additional security questions, but the data alone does not establish why a particular target was selected or whether a specific security measure would have prevented an incident.



Those questions would require additional variables describing factors such as:



\- access control;

\- security staffing;

\- protective barriers;

\- surveillance;

\- response times;

\- attacker planning;

\- facility design;

\- prior threats;

\- security procedures.



\---



## 18. Correlation vs. Causation



The analysis identifies patterns and associations within the available data.



It does \*\*not\*\* establish that a particular target characteristic, weapon type, geographic location, or security condition caused an incident.



For example, a higher number of incidents involving a particular target category does not by itself demonstrate that those locations had weaker security.



Additional evidence would be necessary before making that conclusion.



This distinction is particularly important when translating descriptive analysis into security recommendations.



\---



# Limitations



## 19. Analytical Limitations



Several limitations should be considered when interpreting the project:



\- The datasets represent specific reporting periods and should not automatically be interpreted as current incident conditions.

\- Missing geographic coordinates affect map completeness.

\- Many firearm records do not identify a specific firearm subtype.

\- Different source datasets may use different definitions and collection methodologies.

\- Casualty totals measure consequences but do not independently measure the effectiveness of security controls.

\- Target categories are broad and may contain very different environments.

\- The available data does not contain every variable necessary to determine why an incident occurred.

\- Observed relationships should not automatically be interpreted as causal relationships.



These limitations do not make the dataset unusable. Instead, they define what conclusions the evidence can reasonably support.



\---



# Conclusion



This project demonstrates how violent-event data can be transformed from raw incident records into a structured analytical model for examining firearm incidents, casualty severity, target environments, attack methods, and geographic patterns.



The analysis identified \*\*1,718 firearm incidents\*\*, including \*\*384 incidents with five or more total casualties\*\*. The analytical security filter identified \*\*1,629 security-relevant firearm incidents\*\*, including \*\*367 high-severity incidents\*\*.



The project also demonstrated that data-quality findings are themselves analytically important. Missing coordinates, unknown firearm subtypes, and incomplete contextual information directly affect what questions can responsibly be answered.



Rather than hiding these limitations, they are documented as part of the final analysis.



The technical implementation—including Python preprocessing, validation, AWS S3, Snowflake, dbt, SQL modeling, and Power BI—is documented separately in:



## \[Technical Documentation → readme\_tech.md](readme\_tech.md)



The main project landing page is available here:



## \[← Return to README](README.md)



