# MySQL-ready Dataset Preparation

After cleaning and standardizing the category-wise datasets, MySQL-ready CSV files were created.

## Common Structure

Each MySQL-ready file follows the same 16-column structure:

1. review_id
2. category
3. market_place
4. customer_id
5. product_id
6. product_parent
7. product_title
8. star_rating
9. helpful_votes
10. total_votes
11. vine
12. verified_purchase
13. review_headline
14. review_body
15. review_date
16. sentiment

## Prepared Files

The following category-wise files were prepared:

- `amazon_books_mysql.csv`
- `amazon_ebook_mysql.csv`
- `amazon_grocery_mysql.csv`
- `amazon_beauty_mysql.csv`
- `amazon_electronics_mysql.csv`

## Purpose

The files were prepared with a consistent structure so that datasets from different categories could be integrated into one centralized MySQL table.

## Validation

Before integration, the files were checked for:

- Correct column count
- Correct column names
- Record count
- Rating values
- Missing values
- Data consistency
- CSV structure

## Result

The standardized files were ready for the next stage:

**MySQL Database Integration**
