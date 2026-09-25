# Category-wise Data Integration

## Integration Approach

After the Books dataset was successfully integrated and validated, the same Python-to-MySQL batch insertion process was applied to the remaining category datasets.

The process was kept consistent across categories so that all datasets could be stored in the same centralized table.

## Common Integration Process

For each category:

1. Load the MySQL-ready CSV using Pandas.
2. Replace missing Pandas values with `None` so they are stored as SQL `NULL`.
3. Connect to the `amazon_customer_feedback` database using `mysql-connector-python`.
4. Insert records into the `amazon_feedback` table.
5. Use batch insertion with a batch size of 5,000 records.
6. Commit the inserted records.
7. Validate the category record count.
8. Check the integrated data using SQL queries.

## Categories Integrated

The same integration process was applied to:

- Books
- Ebook
- Grocery
- Beauty
- Electronics

## Final Category-wise Record Counts

| Category | Records |
|---|---:|
| Books | 100,100 |
| Ebook | 100,100 |
| Grocery | 180,018 |
| Beauty | 127,483 |
| Electronics | 153,672 |
| **Total** | **661,373** |

## Centralized Database

All category datasets were stored in the same table:

`amazon_feedback`

The `category` field was retained to distinguish the different product categories during SQL analysis.

## Result

The separate category datasets were successfully consolidated into one centralized customer-feedback database.

This enabled cross-category analysis using SQL without maintaining separate database tables for each category.

## Next Stage

The integrated database was used for:

**SQL Analysis → Business Insights → Power BI Dashboard**
