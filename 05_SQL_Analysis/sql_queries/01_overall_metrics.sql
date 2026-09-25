SELECT
    COUNT(*) AS total_reviews,
    COUNT(DISTINCT category) AS total_categories,
    COUNT(DISTINCT product_id) AS unique_products,
    COUNT(DISTINCT customer_id) AS unique_customers,
    ROUND(AVG(star_rating), 2) AS overall_average_rating
FROM amazon_feedback;
