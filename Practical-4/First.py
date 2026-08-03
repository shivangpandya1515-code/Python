import sqlite3

# Connect to SQLite Database
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

print("Database Connected Successfully!")

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")

conn.commit()
print("Table Created Successfully!")

# ------------------------
# CREATE (Insert Record)
# ------------------------
cursor.execute(
    "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
    ("Shivang", 18, "Computer Engineering")
)

cursor.execute(
    "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
    ("Rahul", 19, "Information Technology")
)

conn.commit()
print("\nRecords Inserted Successfully!")

# ------------------------
# READ (Display Records)
# ------------------------
print("\nStudent Records:")

cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

for row in rows:
    print(row)

# ------------------------
# UPDATE Record
# ------------------------
cursor.execute(
    "UPDATE students SET course=? WHERE name=?",
    ("Computer Science", "Rahul")
)

conn.commit()

print("\nRecord Updated Successfully!")

# Display Updated Records
print("\nUpdated Records:")

cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

# ------------------------
# DELETE Record
# ------------------------
cursor.execute(
    "DELETE FROM students WHERE name=?",
    ("Rahul",)
)

conn.commit()

print("\nRecord Deleted Successfully!")

# Display Final Records
print("\nFinal Records:")

cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

# Close Database
conn.close()

print("\nDatabase Connection Closed Successfully!")