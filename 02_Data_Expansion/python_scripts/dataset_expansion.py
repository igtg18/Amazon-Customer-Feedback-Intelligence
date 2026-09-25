import pandas as pd

# Load the initial category dataset
initial_df = pd.read_csv("INITIAL_DATASET.csv")

# Load the additional dataset
additional_df = pd.read_csv("ADDITIONAL_DATASET.csv")

# Combine the datasets
expanded_df = pd.concat(
    [initial_df, additional_df],
    ignore_index=True
)

# Remove exact duplicate records
expanded_df = expanded_df.drop_duplicates()

# Check the resulting dataset
print("Expanded dataset rows:", len(expanded_df))
print("Expanded dataset columns:", expanded_df.columns.tolist())

# Save the expanded dataset
expanded_df.to_csv(
    "EXPANDED_DATASET.csv",
    index=False
)

print("Expanded dataset created successfully!")
