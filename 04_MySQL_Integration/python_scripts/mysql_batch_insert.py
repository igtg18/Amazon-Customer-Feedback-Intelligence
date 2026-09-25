import pandas as pd
import mysql.connector

# MySQL connection
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="YOUR_MYSQL_USER",
    password="YOUR_MYSQL_PASSWORD",
    database="amazon_customer_feedback"
)

cursor = conn.cursor()

# Load MySQL-ready CSV
df = pd.read_csv("MYSQL_READY_DATASET.csv")

# Replace missing values with None for MySQL NULL
df = df.where(pd.notnull(df), None)

# Insert query
insert_query = """
INSERT INTO amazon_feedback (
    review_id,
    category,
    market_place,
    customer_id,
    product_id,
    product_parent,
    product_title,
    star_rating,
    helpful_votes,
    total_votes,
    vine,
    verified_purchase,
    review_headline,
    review_body,
    review_date,
    sentiment
)
VALUES (
    %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s, %s, %s
)
"""

# Batch insertion
batch_size = 5000

for start in range(0, len(df), batch_size):
    batch = df.iloc[start:start + batch_size]

    records = [
        tuple(row)
        for row in batch.itertuples(index=False, name=None)
    ]

    cursor.executemany(insert_query, records)
    conn.commit()

    print(
        f"Inserted {min(start + batch_size, len(df))} "
        f"of {len(df)} records"
    )

cursor.close()
conn.close()

print("Data inserted successfully!")
