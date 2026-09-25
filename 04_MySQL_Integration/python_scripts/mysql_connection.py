import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="YOUR_MYSQL_USER",
    password="YOUR_MYSQL_PASSWORD",
    database="amazon_customer_feedback"
)

if conn.is_connected():
    print("MySQL connection successful!")

conn.close()
print("Connection closed.")
