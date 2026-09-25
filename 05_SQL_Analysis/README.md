# 05 — SQL Analysis

## Objective

The objective of this stage was to analyze the centralized Amazon customer feedback database using SQL.

After integrating the category-wise datasets into the `amazon_feedback` table, SQL queries were used to identify customer feedback patterns, category performance, ratings, sentiment distribution, negative reviews, product-level issues, and customer pain points.

## Database Used

Database:

`amazon_customer_feedback`

Table:

`amazon_feedback`

## Analysis Areas

The SQL analysis covered:

1. Overall database metrics
2. Category-wise review counts
3. Average rating by category
4. Sentiment distribution
5. Sentiment percentage by category
6. Negative review percentage
7. Products with higher numbers of negative reviews
8. Helpful negative reviews
9. Negative-review issue keywords
10. Quality-related issues
11. Product-condition issues
12. Authenticity-related issues
13. Price-related issues
14. Delivery-related issues

## Analysis Approach

The analysis followed this workflow:

```text
Centralized MySQL Database
        ↓
SQL Queries
        ↓
Data Aggregation
        ↓
Category-wise Analysis
        ↓
Issue & Sentiment Analysis
        ↓
Business Findings
