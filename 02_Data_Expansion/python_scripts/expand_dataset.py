import pandas as pd

# Load the initial dataset
initial_df = pd.read_csv("PATH_TO_INITIAL_DATASET")

# Load the additional dataset
additional_df = pd.read_csv("PATH_TO_ADDITIONAL_DATASET")

# Combine the datasets
expanded_df = pd.concat(
    [initial_df, additional_df],
    ignore_index=True
)

# Remove exact duplicate records
expanded_df = expanded_df.drop_duplicates()

# Check the expanded dataset
print("Expanded Rows:", len(expanded_df))
print("Columns:", expanded_df.columns.tolist())

# Save the expanded dataset
expanded_df.to_csv(
    "PATH_TO_EXPANDED_DATASET",
    index=False
)

print("Expanded dataset created successfully!")
