SELECT
    category,
    COUNT(*) AS total_reviews,
    SUM(
        CASE
            WHEN LOWER(sentiment) = 'negative' THEN 1
            ELSE 0
        END
    ) AS negative_reviews,
    ROUND(
        SUM(
            CASE
                WHEN LOWER(sentiment) = 'negative' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS negative_review_percentage
FROM amazon_feedback
GROUP BY category
ORDER BY negative_review_percentage DESC;
