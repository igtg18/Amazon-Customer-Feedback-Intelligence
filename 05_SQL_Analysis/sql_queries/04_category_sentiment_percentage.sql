SELECT
    category,
    ROUND(
        SUM(CASE WHEN LOWER(sentiment) = 'positive' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS positive_percentage,

    ROUND(
        SUM(CASE WHEN LOWER(sentiment) = 'neutral' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS neutral_percentage,

    ROUND(
        SUM(CASE WHEN LOWER(sentiment) = 'negative' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS negative_percentage

FROM amazon_feedback
WHERE sentiment IS NOT NULL
GROUP BY category
ORDER BY category;
