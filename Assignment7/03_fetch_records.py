import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="your_password"
)
cur = conn.cursor()

cur.execute("SELECT * FROM students")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
