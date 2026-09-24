# Data Sources

## Amazon Customer Feedback Intelligence

The project uses publicly available Amazon customer review datasets for analysis.

### Categories Used

| Category | Source / Dataset |
|---|---|
| Books | Amazon Books review dataset + additional Amazon Books review dataset |
| Ebook | Amazon Ebook review dataset |
| Grocery | Amazon Fine Food Reviews dataset |
| Beauty | Amazon Beauty review dataset |
| Electronics | Amazon Electronics review dataset |

## Books Dataset Preparation

The initial Books dataset was downloaded in CSV format and inspected using Excel.

Since the initial dataset contained fewer records than required for the project, an additional Books review dataset was obtained in Parquet format.

The Parquet dataset was inspected using Python and Pandas and then converted into CSV format.

The additional data was subsequently used along with the initial Books dataset during the dataset expansion/preparation stage.

## Data Handling

The original datasets were kept as source data. Processed and expanded datasets were created separately for further analysis.

The datasets were later standardized into a common structure before integration into MySQL.

## Tools Used

- Excel
- Python
- Pandas
- CSV
- Parquet
- MySQL
