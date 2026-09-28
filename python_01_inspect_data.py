import pandas as pd
from pathlib import Path

# ============================================================
# FILE PATHS
# ============================================================

gtd_path = Path(
    r"C:\Users\mexar\OneDrive\DE_Academy\Active Shooter - Global Terrorism\globalterrorismdb_2021.csv"
)

fbi_path = Path(
    r"C:\Users\mexar\OneDrive\DE_Academy\Active Shooter - Global Terrorism\mass_shooting.csv"
)


# ============================================================
# FUNCTION TO INSPECT A CSV
# ============================================================

def inspect_csv(file_path, dataset_name):
    print("\n" + "=" * 80)
    print(f"{dataset_name}")
    print("=" * 80)

    print(f"\nFile: {file_path}")

    # Check that the file exists
    if not file_path.exists():
        print("\nERROR: File not found.")
        return

    # --------------------------------------------------------
    # Load CSV
    # --------------------------------------------------------
    try:
        df = pd.read_csv(
            file_path,
            low_memory=False
        )
    except UnicodeDecodeError:
        print("\nUTF-8 decoding failed. Trying latin-1...")
        df = pd.read_csv(
            file_path,
            encoding="latin-1",
            low_memory=False
        )

    # --------------------------------------------------------
    # Basic information
    # --------------------------------------------------------
    print("\n--- DATASET SIZE ---")
    print(f"Rows:    {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]:,}")

    # --------------------------------------------------------
    # Column names
    # --------------------------------------------------------
    print("\n--- COLUMN NAMES ---")

    for i, column in enumerate(df.columns, start=1):
        print(f"{i:>3}. {column}")

    # --------------------------------------------------------
    # Data types
    # --------------------------------------------------------
    print("\n--- DATA TYPES ---")
    print(df.dtypes)

    # --------------------------------------------------------
    # Missing values
    # --------------------------------------------------------
    print("\n--- MISSING VALUES ---")

    missing = df.isnull().sum()
    missing_percent = (df.isnull().mean() * 100).round(2)

    missing_report = pd.DataFrame({
        "missing_count": missing,
        "missing_percent": missing_percent
    })

    missing_report = missing_report[
        missing_report["missing_count"] > 0
    ].sort_values(
        "missing_count",
        ascending=False
    )

    if missing_report.empty:
        print("No missing values found.")
    else:
        print(missing_report)

    # --------------------------------------------------------
    # Duplicate rows
    # --------------------------------------------------------
    print("\n--- DUPLICATE ROWS ---")
    duplicates = df.duplicated().sum()
    print(f"Duplicate rows: {duplicates:,}")

    # --------------------------------------------------------
    # First 5 rows
    # --------------------------------------------------------
    print("\n--- FIRST 5 ROWS ---")
    print(df.head())

    # --------------------------------------------------------
    # Last 5 rows
    # --------------------------------------------------------
    print("\n--- LAST 5 ROWS ---")
    print(df.tail())

    # --------------------------------------------------------
    # Memory usage
    # --------------------------------------------------------
    memory_mb = df.memory_usage(deep=True).sum() / (1024 ** 2)

    print("\n--- MEMORY USAGE ---")
    print(f"Approximate memory: {memory_mb:,.2f} MB")

    # --------------------------------------------------------
    # Numeric summary
    # --------------------------------------------------------
    print("\n--- NUMERIC SUMMARY ---")
    print(df.describe(include="number").T)

    return df


# ============================================================
# INSPECT GTD DATA
# ============================================================

gtd_df = inspect_csv(
    gtd_path,
    "GLOBAL TERRORISM DATABASE (GTD)"
)


# ============================================================
# INSPECT FBI DATA
# ============================================================

fbi_df = inspect_csv(
    fbi_path,
    "FBI MASS SHOOTING DATA"
)


print("\n" + "=" * 80)
print("INSPECTION COMPLETE")
print("=" * 80)