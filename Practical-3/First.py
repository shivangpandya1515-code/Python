import sqlite3

# Connect to SQLite Database
conn = sqlite3.connect("student.db")

# Create Cursor
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")

print("Table Created Successfully!")

# Insert Records
cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
               ("Shivang", 18, "Computer Engineering"))

cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
               ("Rahul", 19, "Information Technology"))

conn.commit()

print("Records Inserted Successfully!")

# Display Records
print("\nStudent Records")

cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

for row in rows:
    print(row)

# Update Record
cursor.execute("""
UPDATE students
SET course = ?
WHERE name = ?
""", ("Computer Science", "Rahul"))

conn.commit()

print("\nRecord Updated Successfully!")

# Display Updated Records
cursor.execute("SELECT * FROM students")

print("\nUpdated Records")

for row in cursor.fetchall():
    print(row)

# Delete Record
cursor.execute("""
DELETE FROM students
WHERE name = ?
""", ("Rahul",))

conn.commit()

print("\nRecord Deleted Successfully!")

# Display Final Records
cursor.execute("SELECT * FROM students")

print("\nFinal Records")

for row in cursor.fetchall():
    print(row)

# Close Connection
conn.close()

print("\nDatabase Connection Closed.")