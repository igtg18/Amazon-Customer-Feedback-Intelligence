SELECT
    category,
    COUNT(star_rating) AS rated_reviews,
    ROUND(AVG(star_rating), 2) AS average_rating
FROM amazon_feedback
GROUP BY category
ORDER BY average_rating DESC;
