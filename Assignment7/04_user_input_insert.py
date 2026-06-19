import psycopg2

name = input("Enter student name: ")
age = int(input("Enter age: "))

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="your_password"
)
cur = conn.cursor()

cur.execute(
    "INSERT INTO students (name, age) VALUES (%s, %s)",
    (name, age)
)

conn.commit()
print("User data inserted successfully!")

cur.close()
conn.close()
