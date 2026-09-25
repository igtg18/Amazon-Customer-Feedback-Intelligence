# 03 — Data Cleaning and Standardization

## Objective

The objective of this stage was to clean and standardize the expanded Amazon customer review datasets before integrating them into MySQL.

The datasets were collected from different sources, so their structures, column names, formats, and available fields were not always the same.

Therefore, the datasets were processed and converted into a common structure.

## Data Cleaning Process

The main steps performed during this stage were:

1. Inspect the expanded datasets.
2. Check the available columns and data types.
3. Identify missing and inconsistent values.
4. Map different source columns into a common structure.
5. Standardize rating information.
6. Standardize customer, product, and review fields.
7. Standardize sentiment values.
8. Standardize date information.
9. Handle missing values appropriately.
10. Validate the cleaned datasets.
11. Create MySQL-ready CSV files.

## Standardized Dataset Structure

All category datasets were prepared using a common 16-column structure:

| Column |
|---|
| review_id |
| category |
| market_place |
| customer_id |
| product_id |
| product_parent |
| product_title |
| star_rating |
| helpful_votes |
| total_votes |
| vine |
| verified_purchase |
| review_headline |
| review_body |
| review_date |
| sentiment |

## Rating Handling

Rating values were checked during the cleaning process.

Missing rating values were treated as missing values rather than being interpreted as zero-star ratings.

## Sentiment Handling

Sentiment values were standardized so that equivalent sentiment labels used a consistent format across categories.

## MySQL-ready Files

After cleaning and standardization, separate MySQL-ready CSV files were prepared for:

- Books
- Ebook
- Grocery
- Beauty
- Electronics

## Validation

The cleaned datasets were validated by checking:

- Record count
- Column count
- Column names
- Missing values
- Rating values
- Date format
- Sentiment values
- Sample records

## Outcome

The cleaned and standardized datasets were prepared for integration into the centralized MySQL database.

Next stage:

**MySQL Integration → SQL Analysis → Business Insights → Dashboard**
