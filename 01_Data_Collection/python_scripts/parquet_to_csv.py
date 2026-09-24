import pandas as pd

# Path to the additional Books dataset
file_path = r"PATH_TO_PARQUET_FILE"

# Read Parquet dataset
df = pd.read_parquet(file_path)

# Check dataset structure
print("Rows:", len(df))
print("Columns:", df.columns.tolist())

# Convert Parquet to CSV
df.to_csv(
    r"PATH_TO_OUTPUT_CSV",
    index=False
)

print("CSV created successfully!")
