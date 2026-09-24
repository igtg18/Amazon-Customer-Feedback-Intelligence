# 01 — Data Collection

## Objective

The first stage of the Amazon Customer Feedback Intelligence project focused on collecting and organizing Amazon customer-review datasets for five product categories:

- Books
- Ebook
- Grocery
- Beauty
- Electronics

## Data Collection Process

The datasets were collected from publicly available Amazon review sources.

The initial Books dataset was downloaded as a CSV file and inspected using Excel. Since the available data was insufficient for the planned project scope, an additional Books review dataset was obtained in Parquet format.

Python and Pandas were then used to inspect the Parquet dataset and convert it into CSV format.

## Workflow

Initial Dataset
↓
Dataset Inspection
↓
Additional Dataset Acquisition
↓
Parquet-to-CSV Conversion
↓
Category-wise Dataset Expansion
↓
Data Cleaning & Standardization

## Tools Used

- Excel
- Python
- Pandas
- CSV
- Parquet

## Categories

| Category | Data Preparation |
|---|---|
| Books | Initial dataset + additional public review data |
| Ebook | Public review dataset |
| Grocery | Amazon Fine Food review dataset |
| Beauty | Amazon Beauty review dataset |
| Electronics | Amazon Electronics review dataset |

## Outcome

The collected datasets were prepared category-wise and taken forward to the next stage of data cleaning and standardization.
