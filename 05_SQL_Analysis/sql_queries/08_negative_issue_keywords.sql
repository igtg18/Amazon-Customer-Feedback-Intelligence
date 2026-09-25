SELECT
    category,

    SUM(
        CASE
            WHEN LOWER(review_body) LIKE '%quality%'
            THEN 1 ELSE 0
        END
    ) AS quality_mentions,

    SUM(
        CASE
            WHEN LOWER(review_body) LIKE '%broken%'
              OR LOWER(review_body) LIKE '%defective%'
              OR LOWER(review_body) LIKE '%not working%'
            THEN 1 ELSE 0
        END
    ) AS product_condition_mentions,

    SUM(
        CASE
            WHEN LOWER(review_body) LIKE '%fake%'
              OR LOWER(review_body) LIKE '%counterfeit%'
            THEN 1 ELSE 0
        END
    ) AS authenticity_mentions,

    SUM(
        CASE
            WHEN LOWER(review_body) LIKE '%price%'
              OR LOWER(review_body) LIKE '%expensive%'
            THEN 1 ELSE 0
        END
    ) AS price_issue_mentions,

    SUM(
        CASE
            WHEN LOWER(review_body) LIKE '%late delivery%'
              OR LOWER(review_body) LIKE '%delivery%'
            THEN 1 ELSE 0
        END
    ) AS delivery_issue_mentions

FROM amazon_feedback
WHERE LOWER(sentiment) = 'negative'
GROUP BY category
ORDER BY category;
