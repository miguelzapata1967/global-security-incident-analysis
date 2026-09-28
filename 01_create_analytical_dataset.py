import pandas as pd
from pathlib import Path

# Find the project folder
project_folder = Path(__file__).parent


# Find the GTD dataset
file_path = project_folder / "globalterrorismdb_2021.csv"

# Load the GTD dataset
df = pd.read_csv(file_path, low_memory=False)

print("Original rows:", len(df))
print("Original columns:", len(df.columns))

# Columns selected for physical-security analysis
analytical_columns = [
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
    "specificity",
    "vicinity",
    "location",
    "attacktype1_txt",
    "targtype1_txt",
    "targsubtype1_txt",
    "target1",
    "corp1",
    "weaptype1_txt",
    "weapsubtype1_txt",
    "weapdetail",
    "success",
    "suicide",
    "multiple",
    "nkill",
    "nkillus",
    "nkillter",
    "nwound",
    "nwoundus",
    "nwoundte",
    "gname",
    "gsubname",
    "individual",
    "nperps",
    "property",
    "propextent_txt",
    "propvalue",
    "summary",
    "motive",
    "claimed"
]

# Create analytical dataset
analytical_df = df[analytical_columns].copy()

print("\nAnalytical dataset:")
print("Rows:", len(analytical_df))
print("Columns:", len(analytical_df.columns))

print("\nSelected columns:")
print(analytical_df.columns.tolist())

print("\nAttack Types:")
print(analytical_df["attacktype1_txt"].value_counts())

print("\nTarget Types:")
print(analytical_df["targtype1_txt"].value_counts())

print("\nWeapon Types:")
print(analytical_df["weaptype1_txt"].value_counts())

print("\nFirearm incidents:")
firearms = analytical_df[
    analytical_df["weaptype1_txt"] == "Firearms"
]

print("Number of firearm incidents:", len(firearms))

print("\nFirearm incidents by target:")
print(firearms["targtype1_txt"].value_counts())

print("\nFirearm incidents by attack type:")
print(firearms["attacktype1_txt"].value_counts())

print("\nFirearm casualty summary:")
print(firearms[["nkill", "nwound"]].describe())

print("\nFirearm casualty thresholds:")

firearms = analytical_df[
    analytical_df["weaptype1_txt"] == "Firearms"
].copy()

firearms["total_casualties"] = (
    firearms["nkill"].fillna(0) +
    firearms["nwound"].fillna(0)
)

print("\nTotal casualties per firearm incident:")
print(firearms["total_casualties"].describe())

print("\nIncidents with at least 1 death:")
print((firearms["nkill"].fillna(0) >= 1).sum())

print("\nIncidents with at least 5 deaths:")
print((firearms["nkill"].fillna(0) >= 5).sum())

print("\nIncidents with at least 10 deaths:")
print((firearms["nkill"].fillna(0) >= 10).sum())

print("\nIncidents with at least 1 casualty:")
print((firearms["total_casualties"] >= 1).sum())

print("\nHigh-severity firearm incidents:")

high_severity = firearms[
    firearms["total_casualties"] >= 5
].copy()

print("Incidents with 5+ total casualties:", len(high_severity))

print("\nHigh-severity incidents by target:")
print(
    high_severity["targtype1_txt"]
    .value_counts()
)

print("\nHigh-severity incidents by attack type:")
print(
    high_severity["attacktype1_txt"]
    .value_counts()
)

print("\nHigh-severity incidents by weapon subtype:")
print(
    high_severity["weapsubtype1_txt"]
    .value_counts()
)

print("\nHigh-severity casualty summary:")
print(
    high_severity[
        ["nkill", "nwound", "total_casualties"]
    ].describe()
)

print("\nPhysical-security target analysis:")

security_targets = [
    "Private Citizens & Property",
    "Business",
    "Government (General)",
    "Government (Diplomatic)",
    "Educational Institution",
    "Religious Figures/Institutions",
    "Transportation",
    "Airports & Aircraft",
    "Maritime",
    "Utilities",
    "Telecommunication",
    "Police",
    "Military",
    "NGO"
]

firearms["security_relevant_target"] = firearms[
    "targtype1_txt"
].isin(security_targets)

print("\nSecurity-relevant firearm incidents:")
print(
    firearms["security_relevant_target"].value_counts()
)

print("\nSecurity-relevant incidents by target:")
print(
    firearms.loc[
        firearms["security_relevant_target"],
        "targtype1_txt"
    ].value_counts()
)

print("\nHigh-severity security-relevant incidents:")

high_security = firearms[
    (firearms["security_relevant_target"]) &
    (firearms["total_casualties"] >= 5)
]

print("Number of incidents:", len(high_security))

print("\nBy target:")
print(
    high_security["targtype1_txt"].value_counts()
)

print("\nExcluded firearm incidents:")

excluded_firearms = firearms[
    ~firearms["security_relevant_target"]
].copy()

print("Number excluded:", len(excluded_firearms))

print("\nExcluded target types:")
print(
    excluded_firearms["targtype1_txt"]
    .value_counts()
)

print("\nExcluded incidents with casualties:")

excluded_firearms["total_casualties"] = (
    excluded_firearms["nkill"].fillna(0) +
    excluded_firearms["nwound"].fillna(0)
)

print(
    excluded_firearms[
        ["targtype1_txt", "attacktype1_txt", "total_casualties"]
    ].sort_values(
        "total_casualties",
        ascending=False
    ).head(20)
)

# ============================================================
# FINAL ANALYTICAL DATASET
# ============================================================

# Keep all firearm-related incidents
firearms_final = analytical_df[
    analytical_df["weaptype1_txt"] == "Firearms"
].copy()

# ------------------------------------------------------------
# 1. Total casualties
# ------------------------------------------------------------

firearms_final["total_casualties"] = (
    firearms_final["nkill"].fillna(0) +
    firearms_final["nwound"].fillna(0)
)

# ------------------------------------------------------------
# 2. Incident severity
# ------------------------------------------------------------

def classify_severity(casualties):
    if casualties == 0:
        return "No Reported Casualties"
    elif casualties <= 4:
        return "Low"
    elif casualties <= 9:
        return "High"
    else:
        return "Critical"


firearms_final["severity_category"] = (
    firearms_final["total_casualties"]
    .apply(classify_severity)
)

# ------------------------------------------------------------
# 3. Target environment
# ------------------------------------------------------------

target_environment_map = {
    "Private Citizens & Property": "Civilian / Public",
    "Business": "Commercial",
    "Government (General)": "Government",
    "Government (Diplomatic)": "Government",
    "Educational Institution": "Education",
    "Religious Figures/Institutions": "Religious",
    "Police": "Law Enforcement",
    "Military": "Military",
    "NGO": "NGO / Nonprofit",
    "Transportation": "Transportation",
    "Airports & Aircraft": "Transportation",
    "Maritime": "Transportation",
    "Utilities": "Critical Infrastructure",
    "Telecommunication": "Critical Infrastructure",
    "Food or Water Supply": "Critical Infrastructure",
    "Journalists & Media": "Media",
    "Terrorists/Non-State Militia": "Conflict / Non-State",
    "Violent Political Party": "Political",
    "Tourists": "Civilian / Public",
    "Other": "Other"
}

firearms_final["target_environment"] = (
    firearms_final["targtype1_txt"]
    .map(target_environment_map)
    .fillna("Other")
)

# ------------------------------------------------------------
# 4. Coordinate quality
# ------------------------------------------------------------

def classify_coordinate_quality(row):
    latitude = row["latitude"]
    longitude = row["longitude"]

    if pd.isna(latitude) or pd.isna(longitude):
        return "Missing"

    if (
        -90 <= latitude <= 90
        and -180 <= longitude <= 180
    ):
        return "Valid"

    return "Invalid"


firearms_final["coordinate_quality"] = firearms_final.apply(
    classify_coordinate_quality,
    axis=1
)

# ------------------------------------------------------------
# Save final analytical dataset
# ------------------------------------------------------------

output_file = Path(__file__).parent / "firearm_security_incidents.csv"

firearms_final.to_csv(
    output_file,
    index=False
)

print("\n" + "=" * 60)
print("FINAL ANALYTICAL DATASET")
print("=" * 60)

print("Rows:", len(firearms_final))
print("Columns:", len(firearms_final.columns))
print("Output:", output_file)

print("\nSeverity distribution:")
print(
    firearms_final["severity_category"]
    .value_counts()
)

print("\nTarget environment distribution:")
print(
    firearms_final["target_environment"]
    .value_counts()
)

print("\nCoordinate quality:")
print(
    firearms_final["coordinate_quality"]
    .value_counts()
)

print("\nFinal dataset created successfully.")

# Export original GTD column names for Snowflake RAW table
with open("gtd_column_names.txt", "w", encoding="utf-8") as f:
    for col in df.columns:
        f.write(f'"{col}" TEXT,\n')

print("GTD column names exported.")

firearms_final["has_casualties"] = (
    firearms_final["total_casualties"] > 0
)

firearms_final["high_severity"] = (
    firearms_final["total_casualties"] >= 5
)

firearms_final["critical_severity"] = (
    firearms_final["total_casualties"] >= 10
)

firearms_final["security_relevant_target"] = (
    firearms_final["targtype1_txt"].isin(security_targets)
)

