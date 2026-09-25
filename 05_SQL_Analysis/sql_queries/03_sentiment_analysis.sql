SELECT
    LOWER(sentiment) AS sentiment,
    COUNT(*) AS review_count
FROM amazon_feedback
WHERE sentiment IS NOT NULL
GROUP BY LOWER(sentiment)
ORDER BY review_count DESC;
