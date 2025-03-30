import psycopg2

# Connect to db

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Create a new db

cur.execute("CREATE DATABASE ")
