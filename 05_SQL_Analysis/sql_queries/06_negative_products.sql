SELECT
    category,
    product_id,
    product_title,
    COUNT(*) AS negative_reviews,
    ROUND(AVG(star_rating), 2) AS average_rating,
    SUM(helpful_votes) AS total_helpful_votes
FROM amazon_feedback
WHERE LOWER(sentiment) = 'negative'
GROUP BY
    category,
    product_id,
    product_title
ORDER BY negative_reviews DESC;
