# SQL Analysis

## Objective

To analyze the integrated Amazon customer feedback dataset using MySQL and identify category performance, customer sentiment, negative-review patterns, product-level issues, and major customer pain points.

## Analysis Performed

### 1. Overall Database Metrics
- Total reviews
- Number of categories
- Unique products
- Unique customers
- Overall average rating

### 2. Category-wise Rating Analysis
Calculated the average customer rating for each product category.

### 3. Overall Sentiment Analysis
Analyzed the distribution of positive, negative, and neutral reviews.

### 4. Category-wise Sentiment Analysis
Calculated positive, neutral, and negative sentiment percentages for each category.

### 5. Negative Review Analysis
Identified categories with higher volumes and percentages of negative reviews.

### 6. Negative Product Analysis
Identified products receiving a higher number of negative reviews within each category.

### 7. Helpful Negative Reviews
Analyzed negative reviews with high helpful-vote counts to identify customer issues that received significant customer attention.

### 8. Negative Issue / Keyword Analysis
Analyzed negative reviews for issue-related keywords such as:
- Quality
- Product condition
- Authenticity
- Price
- Delivery

## Key Metrics Identified

- Total reviews: 661,373
- Total categories: 5
- Unique products: 255,229
- Unique customers: 423,006
- Overall average rating: approximately 4.01

## Tools Used

- MySQL
- MySQL Workbench
- SQL
- Python
- Pandas

## Outcome

The SQL analysis transformed the integrated review data into measurable customer-feedback metrics. These results will be used for the next stage: **Business Insights**, where the analytical findings will be converted into business-relevant observations and actions.
