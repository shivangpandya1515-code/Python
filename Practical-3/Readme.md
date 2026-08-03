# 🗄️ SQLite Database Connection and Basic SQL

A simple Python project that demonstrates how to connect to an SQLite database and perform basic SQL operations such as **Create, Insert, Select, Update, and Delete (CRUD)** using Python's built-in `sqlite3` module.

---

## 📌 Objective

To implement and understand SQLite Database Connection and Basic SQL operations using Python.

---

## 🚀 Features

- Connect to an SQLite database
- Create a database table
- Insert records
- Retrieve records
- Update existing records
- Delete records
- Display database contents
- Close the database connection safely

---

## 🛠️ Technologies Used

- Python 3.x
- SQLite3 (Built-in Python Module)

---

## 📂 Project Structure

```
SQLite-Database-Connection/
│
├── main.py              # Python source code
├── student.db           # SQLite database (created automatically)
└── README.md            # Project documentation
```

---

## 💻 Requirements

- Python 3.x installed

No additional libraries are required because **sqlite3** comes with Python.

---

## ▶️ How to Run

### Step 1

Clone this repository

```bash
git clone https://github.com/your-username/SQLite-Database-Connection.git
```

### Step 2

Navigate to the project folder

```bash
cd SQLite-Database-Connection
```

### Step 3

Run the program

```bash
python main.py
```

---

## 📚 SQL Operations Implemented

### 1️⃣ Create Table

```sql
CREATE TABLE students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER,
course TEXT
);
```

---

### 2️⃣ Insert Data

```sql
INSERT INTO students(name, age, course)
VALUES('Shivang',18,'Computer Engineering');
```

---

### 3️⃣ Select Data

```sql
SELECT * FROM students;
```

---

### 4️⃣ Update Data

```sql
UPDATE students
SET course='Computer Science'
WHERE name='Rahul';
```

---

### 5️⃣ Delete Data

```sql
DELETE FROM students
WHERE name='Rahul';
```

---

## 📸 Expected Output

```
Table Created Successfully!

Records Inserted Successfully!

Student Records

(1, 'Shivang', 18, 'Computer Engineering')
(2, 'Rahul', 19, 'Information Technology')

Record Updated Successfully!

Updated Records

(1, 'Shivang', 18, 'Computer Engineering')
(2, 'Rahul', 19, 'Computer Science')

Record Deleted Successfully!

Final Records

(1, 'Shivang', 18, 'Computer Engineering')

Database Connection Closed.
```

---

## 📖 Concepts Covered

- SQLite Database
- Database Connection
- SQL Queries
- CRUD Operations
- Python sqlite3 Module
- Database Cursor
- Commit Transactions
- Fetch Records

---

## 🌟 Advantages

- Lightweight database
- No separate server required
- Easy to learn
- Built into Python
- Fast and portable
- Suitable for desktop and student projects

---

## 🎯 Applications

- Student Management Systems
- Library Management
- Inventory Systems
- Desktop Applications
- Local Data Storage
- Learning SQL

---

## 📌 Future Enhancements

- Add a graphical user interface (GUI)
- Implement search functionality
- Add user authentication
- Export records to CSV or Excel
- Connect with a web application

---

## 👨‍💻 Author

**Shivang Pandya**

Diploma in Computer Engineering

---

## 📄 License

This project is created for educational and learning purposes.