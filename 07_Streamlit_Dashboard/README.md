# Streamlit Dashboard

## Project Overview

The Amazon Customer Feedback Intelligence dashboard is an interactive analytics application developed using Python and Streamlit. It presents customer feedback findings across five Amazon product categories.

## Dashboard Pages

### 1. Executive Overview
- Displays overall dataset KPIs.
- Compares average customer ratings by category.
- Visualizes review volume across categories.
- Provides a category summary.

### 2. Sentiment Intelligence
- Compares positive, neutral, and negative sentiment.
- Displays negative review counts by category.
- Helps identify categories requiring further investigation.

### 3. Product Issues
- Visualizes keyword-based indicators for product quality, product condition, authenticity, and price.
- Presents available keyword counts from the earlier SQL analysis.
- Supports further investigation of customer complaints.

### 4. Business Insights
- Highlights the highest-rated and lowest-rated categories.
- Identifies categories with higher negative sentiment.
- Presents recommendations for further investigation and customer-experience improvement.

## Technology Stack

- Python
- Streamlit
- Pandas
- Plotly
- MySQL — used for the preceding data integration and SQL analysis stages

## Dataset Summary

- Total reviews: 661,373
- Product categories: 5
- Unique products: 255,229
- Unique customers: 423,006
- Overall average rating: 4.01 / 5

## Key Findings

- Books has the highest average rating at 4.34/5.
- Electronics has the lowest average rating at 3.59/5.
- Electronics has the highest negative sentiment percentage at 29.52%.
- Keyword-based issue analysis provides indicators for further investigation.

## Implementation Notes

The current Streamlit prototype uses prepared summary values derived from the completed SQL analysis. It does not yet refresh its metrics through a live MySQL connection.

Keyword counts are indicators rather than confirmed root causes, and issue counts are not available for every category.

## Run the Dashboard Locally

Install the required packages:

```bash
python -m pip install streamlit pandas plotly
```

Run the application from the folder containing `app.py`:

```bash
python -m streamlit run app.py
```

The dashboard will open in your browser at `http://localhost:8501`.

## Project Status

Completed: initial four-page dashboard prototype, category filtering, rating and sentiment visualizations, keyword-based issue analysis, and business recommendations.

Future improvement: connect the application directly to MySQL and calculate dashboard metrics dynamically.
