import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="your_password"
)
cur = conn.cursor()

cur.execute(
    "INSERT INTO students (name, age) VALUES (%s, %s)",
    ("Siddharth", 22)
)

conn.commit()
print("Record inserted successfully!")

cur.close()
conn.close()
