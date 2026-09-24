# Data Sources and Collection Process

## Amazon Customer Feedback Intelligence

The project uses publicly available Amazon customer review datasets across multiple product categories.

The objective of this stage was to collect sufficient review data for each category and prepare the datasets for further processing and analysis.

## Categories Covered

The project includes the following Amazon product categories:

- Books
- Ebook
- Grocery
- Beauty
- Electronics

## Data Collection Process

For each category, an initial dataset was collected and inspected.

When the available data for a category was not sufficient for the planned analysis, an additional dataset from the same category was collected.

The additional datasets were available in different file formats, including CSV and Parquet.

The Parquet datasets were converted into CSV format using Python and Pandas.

The initial and additional datasets belonging to the same category were then used during the dataset expansion and preparation process.

This process was repeated category-wise for the project datasets.

## General Workflow

Initial Dataset
↓
Dataset Inspection
↓
Check Data Availability
↓
Collect Additional Dataset for Same Category
↓
Convert Parquet Dataset to CSV if Required
↓
Combine / Prepare Category-wise Data
↓
Create Expanded Dataset
↓
Validate Dataset
↓
Proceed to Data Cleaning and Standardization

## Category-wise Collection

| Category | Initial Dataset | Additional Dataset | Processing |
|---|---|---|---|
| Books | Collected | Collected | CSV / Parquet conversion / expansion |
| Ebook | Collected | Collected | CSV / Parquet conversion / expansion |
| Grocery | Collected | Collected | Dataset preparation / expansion |
| Beauty | Collected | Collected | Dataset preparation / expansion |
| Electronics | Collected | Collected | Dataset preparation / expansion |

## Dataset Expansion

The purpose of collecting additional datasets was to increase the available review records for each category.

The datasets were not forced to have the same number of records.

Each category was prepared based on the amount of genuine review data available from the collected sources.

Therefore, the final category-wise datasets contain different numbers of records.

## Data Preservation

The original source datasets were kept separate from the processed datasets.

Processed and expanded datasets were created as separate files so that the original source data remained unchanged.

## Tools Used

- Excel
- Python
- Pandas
- CSV
- Parquet
- MySQL

## Outcome

At the end of the data collection and initial preparation stage, sufficient category-wise Amazon review data was collected and prepared for the next stages of the project.

The prepared datasets were then taken forward for data cleaning, standardization, MySQL integration, SQL analysis, and business insights.
