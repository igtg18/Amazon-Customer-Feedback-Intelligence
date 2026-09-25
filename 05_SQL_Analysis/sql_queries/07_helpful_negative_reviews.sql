SELECT
    category,
    product_id,
    product_title,
    star_rating,
    helpful_votes,
    review_headline,
    review_body
FROM amazon_feedback
WHERE LOWER(sentiment) = 'negative'
ORDER BY helpful_votes DESC
LIMIT 30;
