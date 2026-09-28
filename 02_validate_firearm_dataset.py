import pandas as pd
from pathlib import Path


# ============================================================
# LOAD FINAL DATASET
# ============================================================

input_file = Path(__file__).parent / "firearm_security_incidents.csv"

df = pd.read_csv(input_file)


print("=" * 60)
print("FINAL DATASET QUALITY CONTROL")
print("=" * 60)

print("\nDataset:")
print("Rows:", len(df))
print("Columns:", len(df))


# ============================================================
# 1. DUPLICATE EVENT IDs
# ============================================================

duplicate_eventids = df["eventid"].duplicated().sum()

print("\n1. Duplicate eventid values:")
print(duplicate_eventids)


# ============================================================
# 2. NULL VALUES
# ============================================================

print("\n2. Columns with missing values:")

null_counts = df.isnull().sum()

null_counts = null_counts[null_counts > 0]

if len(null_counts) == 0:
    print("No missing values.")
else:
    print(null_counts)


# ============================================================
# 3. DATA TYPES
# ============================================================

print("\n3. Data types:")
print(df.dtypes)


# ============================================================
# 4. CASUALTY CALCULATION VALIDATION
# ============================================================

expected_casualties = (
    df["nkill"].fillna(0) +
    df["nwound"].fillna(0)
)

casualty_errors = (
    df["total_casualties"] != expected_casualties
).sum()

print("\n4. Total casualty calculation errors:")
print(casualty_errors)


# ============================================================
# 5. SEVERITY VALIDATION
# ============================================================

def expected_severity(casualties):

    if casualties == 0:
        return "No Reported Casualties"

    elif casualties <= 4:
        return "Low"

    elif casualties <= 9:
        return "High"

    else:
        return "Critical"


expected_severity_values = (
    df["total_casualties"]
    .apply(expected_severity)
)

severity_errors = (
    df["severity_category"] != expected_severity_values
).sum()

print("\n5. Severity classification errors:")
print(severity_errors)


# ============================================================
# 6. TARGET ENVIRONMENT VALIDATION
# ============================================================

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

expected_environment = (
    df["targtype1_txt"]
    .map(target_environment_map)
    .fillna("Other")
)

environment_errors = (
    df["target_environment"] != expected_environment
).sum()

print("\n6. Target environment classification errors:")
print(environment_errors)


# ============================================================
# 7. COORDINATE VALIDATION
# ============================================================

invalid_latitude = (
    df["latitude"].notna() &
    ~df["latitude"].between(-90, 90)
).sum()

invalid_longitude = (
    df["longitude"].notna() &
    ~df["longitude"].between(-180, 180)
).sum()

print("\n7. Coordinate validation:")
print("Invalid latitude:", invalid_latitude)
print("Invalid longitude:", invalid_longitude)


# ============================================================
# 8. COORDINATE QUALITY VALIDATION
# ============================================================

expected_coordinate_quality = []

for _, row in df.iterrows():

    latitude = row["latitude"]
    longitude = row["longitude"]

    if pd.isna(latitude) or pd.isna(longitude):

        expected_coordinate_quality.append("Missing")

    elif (
        -90 <= latitude <= 90
        and -180 <= longitude <= 180
    ):

        expected_coordinate_quality.append("Valid")

    else:

        expected_coordinate_quality.append("Invalid")


coordinate_quality_errors = (
    df["coordinate_quality"]
    != expected_coordinate_quality
).sum()

print("\n8. Coordinate quality classification errors:")
print(coordinate_quality_errors)


# ============================================================
# 9. FIREARM VALIDATION
# ============================================================

non_firearm_records = (
    df["weaptype1_txt"] != "Firearms"
).sum()

print("\n9. Non-firearm records:")
print(non_firearm_records)


# ============================================================
# 10. FINAL VALIDATION SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("VALIDATION SUMMARY")
print("=" * 60)

print("Expected rows: 1718")
print("Actual rows:", len(df))

print("Expected columns: 44")
print("Actual columns:", len(df.columns))

print("Duplicate eventids:", duplicate_eventids)
print("Casualty errors:", casualty_errors)
print("Severity errors:", severity_errors)
print("Target environment errors:", environment_errors)
print("Invalid latitude:", invalid_latitude)
print("Invalid longitude:", invalid_longitude)
print("Coordinate quality errors:", coordinate_quality_errors)
print("Non-firearm records:", non_firearm_records)

print("\nValidation complete.")