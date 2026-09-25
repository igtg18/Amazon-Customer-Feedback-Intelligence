# 04 — MySQL Database Integration

## Objective

The objective of this stage was to create a centralized MySQL database and integrate the cleaned, standardized Amazon customer feedback datasets into a common table.

The category-wise datasets were prepared using the same 16-column structure so that they could be stored and analyzed together.

## Database Setup

A MySQL database was created with the name:

`amazon_customer_feedback`

A centralized table was created:

`amazon_feedback`

## Common Table Structure

The table contains the following 16 columns:

- review_id
- category
- market_place
- customer_id
- product_id
- product_parent
- product_title
- star_rating
- helpful_votes
- total_votes
- vine
- verified_purchase
- review_headline
- review_body
- review_date
- sentiment

## Integration Process

The following process was followed:

1. Create the MySQL database.
2. Create the centralized `amazon_feedback` table.
3. Configure MySQL for data loading.
4. Establish Python-to-MySQL connectivity.
5. Prepare category-wise MySQL-ready CSV files.
6. Insert the datasets into the centralized table.
7. Integrate the categories one by one.
8. Validate record counts and data quality.
9. Check rating and category distributions.

## Category Integration

The following categories were integrated:

- Books
- Ebook
- Grocery
- Beauty
- Electronics

The categories were inserted into the same centralized table while retaining the category field for category-level analysis.

## Data Loading

Python and `mysql-connector-python` were used to establish the database connection and insert records in batches.

Batch insertion was used to handle the datasets efficiently instead of inserting all records at once.

## Validation

After integration, the database was validated using SQL queries to check:

- Total record count
- Category-wise record count
- Rating values
- Average rating
- Sample records
- Missing values

## Outcome

The category-wise Amazon customer feedback datasets were successfully integrated into a centralized MySQL database.

The centralized database became the foundation for the next stage:

**SQL Analysis → Business Insights → Power BI Dashboard**
