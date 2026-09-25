import pandas as pd

# Load the expanded dataset
df = pd.read_csv("EXPANDED_DATASET.csv")

# Inspect the dataset
print("Rows:", len(df))
print("Columns:", df.columns.tolist())

# Standardize column names
df.columns = df.columns.str.strip().str.lower()

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check rating values
if "rating" in df.columns:
    print("\nRating values:")
    print(df["rating"].value_counts(dropna=False))

# Remove exact duplicate records
df = df.drop_duplicates()

# Save the cleaned dataset
df.to_csv("CLEANED_DATASET.csv", index=False)

print("\nCleaned dataset created successfully!")
