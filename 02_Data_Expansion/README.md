# 02 — Dataset Expansion

## Objective

The objective of this stage was to increase the number of genuine customer review records available for each Amazon product category.

The initial datasets collected for the project did not contain sufficient records for the planned analysis. Therefore, additional datasets belonging to the same category were collected and processed.

The datasets were expanded category-wise without forcing every category to have the same number of records.

## Expansion Process

The following process was followed for each category:

1. Review the initial dataset.
2. Check the number of available records.
3. Collect an additional dataset for the same category.
4. Inspect the additional dataset using Python and Pandas.
5. Convert Parquet files to CSV when required.
6. Map the available fields to the required project structure.
7. Combine or prepare the initial and additional data.
8. Create a separate expanded dataset.
9. Validate the expanded dataset.
10. Preserve the original datasets separately.

## General Workflow

Initial Category Dataset
↓
Check Record Availability
↓
Collect Additional Same-Category Dataset
↓
Inspect Additional Dataset
↓
Convert Parquet to CSV if Required
↓
Combine / Prepare Data
↓
Create Expanded Dataset
↓
Validate Record Count and Columns
↓
Save Expanded Dataset

## Category-wise Expansion

| Category | Final Expanded Records |
|---|---:|
| Books | 100,100 |
| Ebook | 100,100 |
| Grocery | 180,018 |
| Beauty | 127,483 |
| Electronics | 153,672 |

## Books

The initial Books dataset was first collected as a CSV file.

Since the initial dataset contained fewer records than required, an additional Books review dataset was collected in Parquet format.

Python and Pandas were used to inspect the Parquet dataset and convert it into CSV format.

The additional Books data was then used along with the initial Books data during the expansion/preparation process.

Final prepared Books dataset:

**100,100 records**

## Ebook

The same overall expansion approach was followed for the Ebook category.

An additional Ebook review dataset was collected and processed before creating the expanded Ebook dataset.

Final prepared Ebook dataset:

**100,100 records**

## Grocery

Additional Grocery review data was collected and processed to increase the available records for analysis.

The Grocery dataset was prepared separately and retained its own category-specific record count.

Final prepared Grocery dataset:

**180,018 records**

## Beauty

Additional Beauty review data was collected and processed using the same overall category-wise expansion approach.

A genuine sample of the available source reviews was selected during preparation to create a manageable project dataset.

Final prepared Beauty dataset:

**127,483 records**

## Electronics

Additional Electronics review data was collected and processed using the same category-wise expansion approach.

A genuine sample of the available source reviews was selected during preparation to create a manageable project dataset.

Final prepared Electronics dataset:

**153,672 records**

## Important Data Handling Principle

The project did not artificially create customer reviews or generate synthetic review records.

The expanded datasets were prepared from genuine publicly available review data.

Different categories were allowed to have different record counts based on the available source data and project requirements.

## Output

The output of this stage was a separate expanded dataset for each category.

These expanded datasets were then taken forward to the next stages:

**Data Cleaning → Data Standardization → MySQL Integration → SQL Analysis**
