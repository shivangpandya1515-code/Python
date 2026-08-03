# 🗄️ SQLite CRUD using Parameterized Queries

A simple Python project that demonstrates **CRUD (Create, Read, Update, Delete)** operations using **SQLite Database** with **Parameterized Queries**. This project shows how to securely interact with a database by preventing SQL Injection attacks using placeholders (`?`).

---

## 📌 Objective

To implement and understand **SQLite CRUD operations** using **Parameterized Queries** in Python.

---

## 🚀 Features

- 📂 Connect to SQLite Database
- 🏗️ Create a Table
- ➕ Insert Records
- 📖 Read Records
- ✏️ Update Records
- ❌ Delete Records
- 🔒 Secure Parameterized Queries
- 💾 Commit Changes
- 🔚 Close Database Connection

---

## 🛠️ Technologies Used

- Python 3.x
- SQLite3 (Built-in Python Module)

---

## 📂 Project Structure

```
SQLite-CRUD-Parameterized/
│
├── main.py
├── student.db        # Created automatically
└── README.md
```

---

## 💻 Requirements

- Python 3.x
- Visual Studio Code (Recommended)

> No additional libraries are required because **sqlite3** is included with Python.

---

## ▶️ How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/SQLite-CRUD-Parameterized.git
```

### Step 2: Open the Project Folder

```bash
cd SQLite-CRUD-Parameterized
```

### Step 3: Run the Program

```bash
python main.py
```

---

# 📖 Program Workflow

1. Connect to SQLite Database.
2. Create the `students` table if it doesn't exist.
3. Insert records using parameterized queries.
4. Display all records.
5. Update an existing record.
6. Display updated records.
7. Delete a record.
8. Display final records.
9. Close the database connection.

---

# 🔒 Parameterized Query Example

## Insert Record

```python
cursor.execute(
    "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
    ("Shivang", 18, "Computer Engineering")
)
```

---

## Read Record

```python
cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

for row in rows:
    print(row)
```

---

## Update Record

```python
cursor.execute(
    "UPDATE students SET course=? WHERE name=?",
    ("Computer Science", "Rahul")
)
```

---

## Delete Record

```python
cursor.execute(
    "DELETE FROM students WHERE name=?",
    ("Rahul",)
)
```

---

# 🔐 Why Use Parameterized Queries?

Instead of writing:

```python
cursor.execute(
    "SELECT * FROM students WHERE name='" + name + "'"
)
```

Use:

```python
cursor.execute(
    "SELECT * FROM students WHERE name=?",
    (name,)
)
```

### Benefits

- Prevents SQL Injection attacks
- Automatically escapes user input
- Improves code readability
- Recommended by Python documentation
- Makes database operations more secure

---

# 📸 Sample Output

```
Database Connected Successfully!

Table Created Successfully!

Records Inserted Successfully!

Student Records:
(1, 'Shivang', 18, 'Computer Engineering')
(2, 'Rahul', 19, 'Information Technology')

Record Updated Successfully!

Updated Records:
(1, 'Shivang', 18, 'Computer Engineering')
(2, 'Rahul', 19, 'Computer Science')

Record Deleted Successfully!

Final Records:
(1, 'Shivang', 18, 'Computer Engineering')

Database Connection Closed Successfully!
```

---

# 📚 Concepts Covered

- SQLite Database
- Python sqlite3 Module
- Database Connection
- SQL CRUD Operations
- Parameterized Queries
- SQL Injection Prevention
- Cursor Object
- Transactions (`commit()`)
- Closing Database Connection

---

# 🌟 Advantages

- Secure database operations
- Prevents SQL Injection
- Lightweight and portable
- No external database server required
- Built-in Python support
- Easy to understand and implement

---

# 🎯 Applications

- Student Management System
- Employee Management System
- Library Management System
- Inventory Management System
- Desktop Applications
- Educational Projects

---

# 🔮 Future Enhancements

- Add a Tkinter GUI
- Search and Filter Records
- User Authentication
- Export Data to CSV/Excel
- Integrate with Flask or Django
- Add Input Validation

---

## 👨‍💻 Author

**Shivang Pandya**

Diploma in Computer Engineering

---

## 📄 License

This project is developed for **educational and learning purposes**.