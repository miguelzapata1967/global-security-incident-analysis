import pandas as pd
import os

# ============================================================
# 1. FILE PATHS
# ============================================================

gtd_file = r"C:\Users\mexar\OneDrive\DE_Academy\Active Shooter - Global Terrorism\globalterrorismdb_2021.csv"

output_file = r"C:\Users\mexar\OneDrive\DE_Academy\Active Shooter - Global Terrorism\gtd_cleaned.csv"


# ============================================================
# 2. LOAD RAW GTD DATA
# ============================================================

print("Loading raw GTD data...")

try:
    gtd = pd.read_csv(
        gtd_file,
        low_memory=False,
        encoding="utf-8"
    )
except UnicodeDecodeError:
    gtd = pd.read_csv(
        gtd_file,
        low_memory=False,
        encoding="latin-1"
    )

print(f"Original rows: {len(gtd):,}")
print(f"Original columns: {len(gtd.columns):,}")


# ============================================================
# 3. SELECT ANALYTICAL FIELDS
# ============================================================

primary_fields = [
    # Incident
    "eventid",
    "iyear",
    "imonth",
    "iday",

    # Geography
    "country_txt",
    "region_txt",
    "provstate",
    "city",
    "latitude",
    "longitude",

    # Incident characteristics
    "multiple",
    "success",
    "suicide",
    "attacktype1_txt",

    # Target security
    "targtype1_txt",
    "targsubtype1_txt",
    "corp1",
    "target1",

    # Weapons
    "weaptype1_txt",
    "weapsubtype1_txt",

    # Human impact
    "nkill",
    "nwound",

    # Physical-security consequences
    "property",
    "propextent_txt",
    "ishostkid",
]


# ============================================================
# 4. VERIFY ALL FIELDS EXIST
# ============================================================

missing_fields = [
    field for field in primary_fields
    if field not in gtd.columns
]

if missing_fields:
    print("\nERROR: The following fields were not found:")
    for field in missing_fields:
        print(f" - {field}")

    raise ValueError("One or more analytical fields are missing.")


# ============================================================
# 5. CREATE ANALYTICAL DATASET
# ============================================================

cleaned = gtd[primary_fields].copy()

print(f"\nAnalytical rows: {len(cleaned):,}")
print(f"Analytical columns: {len(cleaned.columns):,}")


# ============================================================
# 6. STANDARDIZE TEXT FIELDS
# ============================================================

text_columns = cleaned.select_dtypes(
    include=["object"]
).columns

for column in text_columns:

    # Remove unnecessary spaces
    cleaned[column] = cleaned[column].str.strip()

    # Convert empty strings to NaN
    cleaned[column] = cleaned[column].replace(
        r"^\s*$",
        pd.NA,
        regex=True
    )


# ============================================================
# 7. FIELD-SPECIFIC GTD CODE HANDLING
# ============================================================
#
# IMPORTANT:
# We are NOT globally replacing every -9/-99/-999.
#
# At this stage we only handle coded values for fields where
# the meaning is appropriate for the analytical dataset.
#
# For numeric impact fields such as nkill and nwound,
# missing values remain missing.
#
# ============================================================


# Property:
# GTD uses coded values for whether property was damaged.
# Keep the original value for now.
#
# We will interpret these values during validation after
# checking the GTD codebook.


# ishostkid:
# Keep original coded values for now.
# Interpretation will be validated before transformation.


# ============================================================
# 8. CREATE DATA-QUALITY FLAGS
# ============================================================

cleaned["nkill_missing_flag"] = cleaned["nkill"].isna()

cleaned["nwound_missing_flag"] = cleaned["nwound"].isna()

cleaned["coordinates_missing_flag"] = (
    cleaned["latitude"].isna() |
    cleaned["longitude"].isna()
)


# ============================================================
# 9. CREATE DATE FIELD
# ============================================================

# Create a date only when year, month, and day are valid.
#
# We do NOT use approximate dates as exact dates.

cleaned["event_date"] = pd.to_datetime(
    {
        "year": cleaned["iyear"],
        "month": cleaned["imonth"],
        "day": cleaned["iday"],
    },
    errors="coerce"
)


# ============================================================
# 10. VALIDATE COORDINATES
# ============================================================

cleaned["coordinates_valid_flag"] = (
    cleaned["latitude"].between(-90, 90, inclusive="both") &
    cleaned["longitude"].between(-180, 180, inclusive="both")
)


# ============================================================
# 11. VALIDATE CASUALTY VALUES
# ============================================================

# Negative casualty values are not treated as valid counts.
# We flag them rather than silently changing them.

cleaned["casualty_value_issue_flag"] = (
    (cleaned["nkill"] < 0) |
    (cleaned["nwound"] < 0)
)


# ============================================================
# 12. DUPLICATE CHECK
# ============================================================

duplicate_count = cleaned.duplicated().sum()

print(f"\nDuplicate rows after transformation: {duplicate_count:,}")


# ============================================================
# 13. DATA-QUALITY SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("DATA QUALITY SUMMARY")
print("=" * 60)

print(
    f"\nFatality information missing: "
    f"{cleaned['nkill_missing_flag'].sum():,}"
)

print(
    f"Injury information missing: "
    f"{cleaned['nwound_missing_flag'].sum():,}"
)

print(
    f"Coordinates missing: "
    f"{cleaned['coordinates_missing_flag'].sum():,}"
)

print(
    f"Invalid coordinate records: "
    f"{(~cleaned['coordinates_valid_flag']).sum():,}"
)

print(
    f"Casualty value issues: "
    f"{cleaned['casualty_value_issue_flag'].sum():,}"
)


# ============================================================
# 14. SAVE CLEANED DATASET
# ============================================================

cleaned.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print("\n" + "=" * 60)
print("CLEANING COMPLETE")
print("=" * 60)

print(f"\nOutput file:")
print(output_file)

print("\nRaw GTD data was NOT modified.")