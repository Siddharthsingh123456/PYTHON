import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="your_password"
)
cur = conn.cursor()

cur.execute("SELECT * FROM students WHERE age > %s", (20,))
print("Filtered Records:")
for row in cur.fetchall():
    print(row)

choice = input("Do you want to truncate the table? (yes/no): ")
if choice.lower() == "yes":
    cur.execute("TRUNCATE TABLE students RESTART IDENTITY")
    conn.commit()
    print("Table truncated successfully!")

cur.close()
conn.close()
