import pandas as pd
from pathlib import Path


# ============================================================
# FILE PATH
# ============================================================

gtd_path = Path(
    r"C:\Users\mexar\OneDrive\DE_Academy\Active Shooter - Global Terrorism\globalterrorismdb_2021.csv"
)


# ============================================================
# LOAD DATA
# ============================================================

print("=" * 80)
print("GTD DATA QUALITY ANALYSIS")
print("=" * 80)

df = pd.read_csv(
    gtd_path,
    low_memory=False
)

print(f"\nRows:    {len(df):,}")
print(f"Columns: {len(df.columns):,}")


# ============================================================
# DEFINE GTD CODED VALUES
# ============================================================
# GTD uses special numeric codes to represent information such
# as unknown, not applicable, or unavailable.
#
# IMPORTANT:
# These are NOT automatically the same as NaN.
# We identify them separately.

gtd_missing_codes = [-9, -99, -999]


# ============================================================
# CREATE DATA QUALITY REPORT
# ============================================================

quality_report = pd.DataFrame({
    "column": df.columns,
    "data_type": df.dtypes.astype(str).values,
    "total_rows": len(df),
    "missing_count": df.isna().sum().values,
    "missing_percent": (
        df.isna().mean().values * 100
    ).round(2),
    "unique_values": df.nunique(dropna=True).values
})


# ============================================================
# COUNT GTD CODED VALUES
# ============================================================

coded_counts = []
coded_percentages = []

for column in df.columns:

    # Only look for coded values in numeric columns
    if pd.api.types.is_numeric_dtype(df[column]):

        coded_count = df[column].isin(gtd_missing_codes).sum()

    else:
        coded_count = 0

    coded_counts.append(coded_count)

    coded_percentages.append(
        round((coded_count / len(df)) * 100, 2)
    )


quality_report["gtd_coded_count"] = coded_counts
quality_report["gtd_coded_percent"] = coded_percentages


# ============================================================
# TOTAL INFORMATION NOT AVAILABLE
# ============================================================
# This combines:
#
# 1. True NaN values
# 2. GTD coded values
#
# We keep these separate above so we don't lose the distinction.

quality_report["total_missing_or_coded"] = (
    quality_report["missing_count"]
    + quality_report["gtd_coded_count"]
)


quality_report["total_missing_or_coded_percent"] = (
    quality_report["total_missing_or_coded"]
    / len(df)
    * 100
).round(2)


# ============================================================
# COMPLETENESS PERCENTAGE
# ============================================================

quality_report["completeness_percent"] = (
    100
    - quality_report["total_missing_or_coded_percent"]
).round(2)


# ============================================================
# SORT BY DATA COMPLETENESS
# ============================================================

quality_report = quality_report.sort_values(
    "total_missing_or_coded_percent",
    ascending=False
)


# ============================================================
# DISPLAY COMPLETE REPORT
# ============================================================

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

print("\n" + "=" * 80)
print("COMPLETE DATA QUALITY REPORT")
print("=" * 80)

print(quality_report.to_string(index=False))


# ============================================================
# SUMMARY
# ============================================================

print("\n" + "=" * 80)
print("DATA QUALITY SUMMARY")
print("=" * 80)

print(
    f"\nColumns with true NaN values: "
    f"{(quality_report['missing_count'] > 0).sum()}"
)

print(
    f"Columns containing GTD coded values: "
    f"{(quality_report['gtd_coded_count'] > 0).sum()}"
)

print(
    f"Columns with 100% missing/coded information: "
    f"{(quality_report['total_missing_or_coded_percent'] == 100).sum()}"
)

print(
    f"Columns with at least 90% complete information: "
    f"{(quality_report['completeness_percent'] >= 90).sum()}"
)


# ============================================================
# EXPORT DATA QUALITY REPORT
# ============================================================

output_path = gtd_path.parent / "gtd_data_quality_report.csv"

quality_report.to_csv(
    output_path,
    index=False
)

print("\n" + "=" * 80)
print("REPORT SAVED")
print("=" * 80)

print(f"\n{output_path}")