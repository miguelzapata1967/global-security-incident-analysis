import pandas as pd
import os

# ============================================================
# 1. FILE PATHS
# ============================================================

gtd_file = r"C:\Users\mexar\OneDrive\DE_Academy\Active Shooter - Global Terrorism\globalterrorismdb_2021.csv"

quality_file = r"C:\Users\mexar\OneDrive\DE_Academy\Active Shooter - Global Terrorism\gtd_data_quality_report.csv"

output_file = r"C:\Users\mexar\OneDrive\DE_Academy\Active Shooter - Global Terrorism\gtd_analytical_scope.csv"


# ============================================================
# 2. LOAD DATA
# ============================================================

print("Loading GTD data...")

gtd = pd.read_csv(
    gtd_file,
    low_memory=False,
    encoding="utf-8"
)

quality = pd.read_csv(quality_file)

print(f"GTD rows: {len(gtd):,}")
print(f"GTD columns: {len(gtd.columns):,}")


# ============================================================
# 3. CREATE ANALYTICAL SCOPE TABLE
# ============================================================

scope = quality.copy()

# Make sure the column name is called "column"
if "column" not in scope.columns:

    # Adjust this if the quality report uses a different name
    possible_names = ["Column", "field", "Field", "column_name"]

    for name in possible_names:
        if name in scope.columns:
            scope = scope.rename(columns={name: "column"})
            break


# ============================================================
# 4. FIELD CATEGORIES
# ============================================================

field_categories = {

    # Incident
    "eventid": "Incident",
    "iyear": "Incident",
    "imonth": "Incident",
    "iday": "Incident",
    "approxdate": "Incident",
    "extended": "Incident",
    "resolution": "Incident",

    # Geography
    "country": "Geography",
    "country_txt": "Geography",
    "region": "Geography",
    "region_txt": "Geography",
    "provstate": "Geography",
    "city": "Geography",
    "latitude": "Geography",
    "longitude": "Geography",
    "specificity": "Geography",
    "vicinity": "Geography",

    # Incident characteristics
    "multiple": "Incident Characteristics",
    "success": "Incident Characteristics",
    "suicide": "Incident Characteristics",
    "attacktype1": "Incident Characteristics",
    "attacktype1_txt": "Incident Characteristics",

    # Target / physical security
    "targtype1": "Target Security",
    "targtype1_txt": "Target Security",
    "targsubtype1": "Target Security",
    "targsubtype1_txt": "Target Security",
    "corp1": "Target Security",
    "target1": "Target Security",

    # Weapons
    "weaptype1": "Weapons",
    "weaptype1_txt": "Weapons",
    "weapsubtype1": "Weapons",
    "weapsubtype1_txt": "Weapons",
    "weapdetail": "Weapons",

    # Impact
    "nkill": "Impact",
    "nwound": "Impact",
    "nkillus": "Impact",
    "nwoundus": "Impact",
    "nkillter": "Impact",
    "nwoundte": "Impact",

    # Security consequences
    "property": "Security Consequences",
    "propextent": "Security Consequences",
    "propextent_txt": "Security Consequences",
    "propvalue": "Security Consequences",
    "propcomment": "Security Consequences",
    "ishostkid": "Security Consequences",
    "nperpcap": "Security Consequences",

    # Threat / perpetrator context
    "gname": "Threat Context",
    "gsubname": "Threat Context",
    "guncertain1": "Threat Context",
    "claimed": "Threat Context",
    "claimmode": "Threat Context",
    "motive": "Threat Context",

    # Supporting evidence
    "summary": "Evidence / Context",
    "scite1": "Evidence / Context",
    "scite2": "Evidence / Context",
    "scite3": "Evidence / Context",
    "addnotes": "Evidence / Context",
}


# ============================================================
# 5. BUSINESS DESCRIPTIONS
# ============================================================

descriptions = {

    "eventid": "Unique identifier for the incident.",
    "iyear": "Year in which the incident occurred.",
    "imonth": "Month in which the incident occurred.",
    "iday": "Day in which the incident occurred.",

    "country_txt": "Country where the incident occurred.",
    "region_txt": "Geographic region where the incident occurred.",
    "provstate": "Province, state, or administrative area.",
    "city": "City where the incident occurred.",
    "latitude": "Latitude of the incident location.",
    "longitude": "Longitude of the incident location.",

    "multiple": "Indicates whether the incident involved multiple attacks.",
    "success": "Indicates whether the attack was successful.",
    "suicide": "Indicates whether the incident involved a suicide attack.",
    "attacktype1_txt": "Primary type of attack.",

    "targtype1_txt": "Primary category of target.",
    "targsubtype1_txt": "More specific category of the primary target.",
    "corp1": "Organization or corporation associated with the target.",
    "target1": "Specific target involved in the incident.",

    "weaptype1_txt": "Primary weapon category.",
    "weapsubtype1_txt": "Primary weapon subtype.",
    "weapdetail": "Detailed description of the weapon used.",

    "nkill": "Number of people killed.",
    "nwound": "Number of people wounded.",
    "nkillus": "Number of U.S. citizens killed.",
    "nwoundus": "Number of U.S. citizens wounded.",
    "nkillter": "Number of perpetrators killed.",
    "nwoundte": "Number of perpetrators wounded.",

    "property": "Indicates whether property was damaged.",
    "propextent_txt": "Estimated extent of property damage.",
    "propvalue": "Estimated value of property damage.",
    "propcomment": "Comments regarding property damage.",
    "ishostkid": "Indicates whether the incident involved hostage taking or kidnapping.",
    "nperpcap": "Number of perpetrators captured.",

    "gname": "Name of the perpetrator group.",
    "guncertain1": "Indicates uncertainty regarding the identified perpetrator group.",
    "claimed": "Indicates whether responsibility was claimed.",
    "claimmode": "Method or mode through which responsibility was claimed.",
    "motive": "Reported motive for the incident.",

    "summary": "Narrative summary of the incident.",
    "scite1": "Primary source citation for the incident.",
    "scite2": "Secondary source citation.",
    "scite3": "Third source citation.",
    "addnotes": "Additional notes about the incident.",
}


# ============================================================
# 6. ANALYTICAL USE DECISIONS
# ============================================================

primary_fields = {
    "eventid",
    "iyear",
    "imonth",
    "iday",

    "country_txt",
    "region_txt",
    "provstate",
    "city",
    "latitude",
    "longitude",

    "multiple",
    "success",
    "suicide",
    "attacktype1_txt",

    "targtype1_txt",
    "targsubtype1_txt",
    "corp1",
    "target1",

    "weaptype1_txt",
    "weapsubtype1_txt",

    "nkill",
    "nwound",
    "nkillter",
    "nwoundte",

    "property",
    "propextent_txt",
    "ishostkid",
    "nperpcap",

    "gname",
    "claimed",
}

supporting_fields = {
    "summary",
    "scite1",
    "scite2",
    "scite3",
    "addnotes",
    "weapdetail",
    "motive",
    "claimmode",
    "guncertain1",
    "specificity",
    "vicinity",
}


# ============================================================
# 7. APPLY ANALYTICAL DECISIONS
# ============================================================

def determine_use(column):

    if column in primary_fields:
        return "Primary"

    if column in supporting_fields:
        return "Supporting"

    return "Excluded from Primary Analysis"


scope["category"] = scope["column"].map(
    field_categories
).fillna("Other / Technical")


scope["business_description"] = scope["column"].map(
    descriptions
).fillna("Not currently selected for the primary security analysis.")


scope["analytical_use"] = scope["column"].apply(
    determine_use
)


# ============================================================
# 8. ADD REASON FOR DECISION
# ============================================================

def decision_reason(row):

    column = row["column"]
    use = row["analytical_use"]

    if use == "Primary":
        return "Directly supports the incident severity, geographic risk, target security, weapon, or physical-security analysis."

    if use == "Supporting":
        return "Useful for context, investigation, validation, or documentation but not required for the primary dashboard analysis."

    return "Not required for the primary analytical questions, highly sparse, redundant, specialized, or outside the defined project scope."


scope["reason"] = scope.apply(
    decision_reason,
    axis=1
)


# ============================================================
# 9. REORDER COLUMNS
# ============================================================

preferred_order = [
    "column",
    "category",
    "business_description",
    "analytical_use",
    "reason",
    "missing_count",
    "missing_percent",
    "gtd_coded_count",
    "gtd_coded_percent",
    "total_missing_or_coded",
    "total_missing_or_coded_percent",
    "completeness_percent",
]

existing_columns = [
    col for col in preferred_order
    if col in scope.columns
]

remaining_columns = [
    col for col in scope.columns
    if col not in existing_columns
]

scope = scope[existing_columns + remaining_columns]


# ============================================================
# 10. SAVE OUTPUT
# ============================================================

scope.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)


# ============================================================
# 11. SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("GTD ANALYTICAL SCOPE COMPLETE")
print("=" * 60)

print(f"\nTotal source fields: {len(scope):,}")

print("\nAnalytical decisions:")

print(
    scope["analytical_use"]
    .value_counts()
    .to_string()
)

print("\nCategories:")

print(
    scope["category"]
    .value_counts()
    .to_string()
)

print(f"\nOutput file:")
print(output_file)

print("\nRaw GTD data was NOT modified.")