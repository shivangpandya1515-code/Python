# 🎓 Practical 7 — Flask CRUD Application with SQLite

## 🚀 Development of a Flask Web Application for Performing CRUD Operations with SQLite Database Integration

---

## 📌 1. Overview

This project implements a **Student Management System** using the **Flask web framework** and **SQLite database**.

The application demonstrates the implementation of the four fundamental database operations:

- ➕ **Create** — Add new student records
- 📖 **Read** — Display existing student records
- ✏️ **Update** — Modify student information
- 🗑️ **Delete** — Remove student records

The project is developed as part of the **Web Development Using Python** practical coursework.

---

## 🎯 2. Objective

The objective of this practical is to develop a Flask-based web application that integrates with an SQLite database and demonstrates complete CRUD functionality.

The practical provides hands-on experience with:

- 🐍 Flask application development
- 🔗 URL routing
- 📝 HTML forms
- 🧩 Jinja2 templates
- 🗄️ SQLite database integration
- 💾 SQL queries
- 🔄 CRUD operations
- 🔐 Parameterized queries
- 📦 Python virtual environments
- 🌐 Git and GitHub

---

## 🛠️ 3. Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 **Python** | Application programming language |
| 🌐 **Flask** | Web application framework |
| 🗄️ **SQLite** | Relational database |
| 🌐 **HTML5** | Web page structure |
| 🧩 **Jinja2** | Server-side template engine |
| 💻 **VS Code** | Development environment |
| 🔧 **Git** | Version control |
| 🐙 **GitHub** | Repository hosting |

---

## ✨ 4. Application Features

The Student Management System provides the following functionality:

- ➕ Add new student records
- 👁️ Display all registered students
- ✏️ Edit existing student information
- 🗑️ Delete student records
- 💾 Store data persistently in SQLite
- ⚙️ Automatically create the database table
- ✅ Validate required form fields
- 🔐 Use parameterized SQL queries
- 🖥️ Provide a simple web-based interface

---

## 🔄 5. CRUD Operations

CRUD represents the four basic operations performed on database records.

| Operation | Description | Implementation |
|-----------|-------------|----------------|
| 🟢 **Create** | Add a new student | `/add` |
| 🔵 **Read** | Display student records | `/` |
| 🟡 **Update** | Modify student information | `/edit/<id>` |
| 🔴 **Delete** | Remove a student | `/delete/<id>` |

---

## 📁 6. Project Structure

```text
Practical-7/
│
├── 🐍 app.py
├── 📖 README.md
├── ⚙️ .gitignore
│
└── 📂 templates/
    ├── 🌐 index.html
    ├── ➕ add.html
    └── ✏️ edit.html
```

### ⚙️ Runtime Files

The following files are generated or maintained locally and are not required to be committed to GitHub:

```text
📄 database.db
📂 venv/
📂 __pycache__/
```

The SQLite database file `database.db` is automatically created when the application is executed.

---

## 📄 7. File Description

### 🐍 `app.py`

The main Flask application containing:

- Flask application configuration
- SQLite database connection
- Database initialization
- Flask routes
- CRUD operations
- Request handling
- Template rendering

### 🌐 `templates/index.html`

Displays all student records in a tabular format and provides options to:

- ➕ Add a student
- ✏️ Edit a student
- 🗑️ Delete a student

### ➕ `templates/add.html`

Provides an HTML form for entering new student information.

### ✏️ `templates/edit.html`

Provides an HTML form for modifying existing student information.

### 🗄️ `database.db`

SQLite database file containing the student records.

This file is generated automatically and is excluded from GitHub using `.gitignore`.

### 📖 `README.md`

Project documentation containing setup instructions, technical details, database structure, testing information, and learning outcomes.

### ⚙️ `.gitignore`

Specifies files and directories that should not be tracked by Git.

---

# 🗄️ 8. Database Design

## 💾 Database

The application uses **SQLite** as its database management system.

```text
Database: database.db
Table: students
```

## 📊 Table Structure

| Column | Data Type | Constraint | Description |
|--------|-----------|------------|-------------|
| `id` | INTEGER | PRIMARY KEY | Unique student identifier |
| `name` | TEXT | NOT NULL | Student name |
| `email` | TEXT | NOT NULL | Student email address |
| `course` | TEXT | NOT NULL | Student course |

The table is created using:

```sql
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    course TEXT NOT NULL
);
```

---

# 💻 9. SQL Operations

## 🟢 9.1 Create

A new student is inserted using:

```sql
INSERT INTO students
(name, email, course)
VALUES (?, ?, ?);
```

## 🔵 9.2 Read

All student records are retrieved using:

```sql
SELECT * FROM students;
```

## 🟡 9.3 Update

Existing student information is modified using:

```sql
UPDATE students
SET name = ?, email = ?, course = ?
WHERE id = ?;
```

## 🔴 9.4 Delete

A student record is removed using:

```sql
DELETE FROM students
WHERE id = ?;
```

---

# 🛣️ 10. Flask Routes

The application defines the following routes:

| Route | HTTP Method | CRUD Operation | Purpose |
|-------|-------------|----------------|---------|
| 🏠 `/` | GET | Read | Display all students |
| ➕ `/add` | GET, POST | Create | Add a new student |
| ✏️ `/edit/<id>` | GET, POST | Update | Edit student information |
| 🗑️ `/delete/<id>` | GET | Delete | Delete a student |

---

# 🔄 11. Application Workflow

```text
                    🚀 Flask Application
                            │
                            ▼
                 🎓 Student Management System
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
       ➕ CREATE          📖 READ           ✏️ UPDATE
          │                 │                 │
          └─────────────────┼─────────────────┘
                            │
                            ▼
                        🗑️ DELETE
                            │
                            ▼
                    🗄️ SQLite Database
```

---

# ▶️ 13. Running the Application

Start the Flask application using:

```bash
python app.py
```

A successful startup will display information similar to:

```text
* Serving Flask app 'app'
* Debug mode: on
* Running on http://127.0.0.1:5000
```

Open a web browser and navigate to:

```text
http://127.0.0.1:5000/
```

The **Student Management System** will then be available.

---

# 🖥️ 14. Using the Application

## ➕ 14.1 Add a Student

Select **Add Student** and enter the required information.

Example:

```text
Name: Rahul Patel
Email: rahul@gmail.com
Course: BCA
```

Submit the form to store the record in the database.

This performs the **Create** operation.

---

## 👁️ 14.2 View Students

The home page displays all records stored in the database.

Example:

| ID | Name | Email | Course | Actions |
|----|------|-------|--------|---------|
| 1 | Rahul Patel | rahul@gmail.com | BCA | ✏️ Edit / 🗑️ Delete |
| 2 | Priya Shah | priya@gmail.com | MCA | ✏️ Edit / 🗑️ Delete |

This performs the **Read** operation.

---

## ✏️ 14.3 Update a Student

Select **Edit** for the required student.

Modify the information and select **Update Student**.

For example:

```text
BCA → MCA
```

The updated record is stored in the database.

This performs the **Update** operation.

---

## 🗑️ 14.4 Delete a Student

Select **Delete** for the required student.

The application displays a confirmation message before removing the record.

Once confirmed, the selected record is deleted from the database.

This performs the **Delete** operation.

---

# 🐍 15. Flask Implementation

## 🔌 Database Connection

The application establishes an SQLite connection using:

```python
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
```

This function is used whenever the application needs to communicate with the database.

---

## 🏗️ Database Initialization

The database is initialized using:

```python
def init_db():
```

The function creates the `students` table if it does not already exist.

---

## 📖 Read Operation

The home route retrieves all student records:

```python
@app.route("/")
def index():
```

The records are then passed to `index.html`.

---

## ➕ Create Operation

The `/add` route handles the creation of new records:

```python
@app.route("/add", methods=["GET", "POST"])
def add():
```

Form data is retrieved using:

```python
request.form
```

and inserted into the database.

---

## ✏️ Update Operation

The `/edit/<id>` route handles modification of existing records:

```python
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
```

The student's ID is used to identify the record that should be updated.

---

## 🗑️ Delete Operation

The `/delete/<id>` route removes a selected record:

```python
@app.route("/delete/<int:id>")
def delete(id):
```

The record is identified using its unique ID.

---

# 🔐 16. Parameterized SQL Queries

The application uses parameterized SQL queries rather than directly inserting user input into SQL statements.

Example:

```python
conn.execute(
    "SELECT * FROM students WHERE id = ?",
    (id,)
)
```

Another example:

```python
conn.execute(
    """
    INSERT INTO students
    (name, email, course)
    VALUES (?, ?, ?)
    """,
    (name, email, course)
)
```

The `?` placeholders allow values to be passed separately from the SQL statement.

This approach improves database security and helps protect against SQL injection.

---

# 🧪 17. Testing

The application can be tested using the following test cases:

| Test Case | Test Action | Expected Result |
|-----------|-------------|-----------------|
| 🧪 TC-01 | Open the application | Home page is displayed |
| 🧪 TC-02 | Open Add Student | Student form is displayed |
| 🧪 TC-03 | Add a student | New record is stored |
| 🧪 TC-04 | View students | Records are displayed |
| 🧪 TC-05 | Edit a student | Record is updated |
| 🧪 TC-06 | Delete a student | Record is removed |
| 🧪 TC-07 | Restart the application | Existing records remain available |

---

# 🖼️ 18. Expected Output

The application displays a student management interface similar to:

```text
🎓 Student Management System

➕ Add Student

--------------------------------------------------------------
ID    Name           Email              Course      Actions
--------------------------------------------------------------
1     Rahul Patel    rahul@gmail.com    BCA         Edit/Delete
2     Priya Shah     priya@gmail.com    MCA         Edit/Delete
--------------------------------------------------------------
```

---

# 🐙 20. Git and GitHub

The project can be managed using Git and hosted on GitHub.

## 1️⃣ Initialize Git

```bash
git init
```

## 2️⃣ Add Project Files

```bash
git add .
```

## 3️⃣ Check Git Status

```bash
git status
```

## 4️⃣ Create the Initial Commit

```bash
git commit -m "Initial commit - Flask CRUD SQLite application"
```

## 5️⃣ Connect the GitHub Repository

```bash
git remote add origin YOUR_GITHUB_REPOSITORY_URL
```

## 6️⃣ Set the Main Branch

```bash
git branch -M main
```

## 7️⃣ Push the Project

```bash
git push -u origin main
```

---

# 🚫 21. Git Ignore Configuration

The `.gitignore` file should contain:

```gitignore
venv/
__pycache__/
*.pyc
database.db
```

This prevents the following from being uploaded to GitHub:

- 📦 Virtual environment
- 🗂️ Python cache files
- 🗄️ Local SQLite database
- 📄 Compiled Python files

---

# 🌐 22. Recommended GitHub Repository Structure

The GitHub repository should contain:

```text
Practical-7-Flask-CRUD/
│
├── ⚙️ .gitignore
├── 📖 README.md
├── 🐍 app.py
│
└── 📂 templates/
    ├── 🌐 index.html
    ├── ➕ add.html
    └── ✏️ edit.html
```

The following files should remain local:

```text
📂 venv/
📄 database.db
📂 __pycache__/
```

---

# 🎓 23. Learning Outcomes

After completing this practical, the following concepts were understood and implemented:

- 🐍 Flask web application development
- 🛣️ Flask routing
- 📡 HTTP GET and POST methods
- 📝 HTML forms
- 🧩 Jinja2 templates
- 🗄️ SQLite database integration
- 💻 SQL table creation
- 🔄 SQL INSERT, SELECT, UPDATE, and DELETE operations
- 🔌 Database connectivity using Python
- 🔐 Parameterized SQL queries
- 📦 Python virtual environments
- 🔧 Git version control
- 🐙 GitHub repository management

---

# 👨‍💻 24. Author

**Shivang Pandya**

**Course:** Web Development Using Python  
**Practical:** 7  
**Project:** Flask CRUD Application with SQLite Database

---

# 📊 Project Summary

| Property | Details |
|----------|---------|
| 🎓 **Project Name** | Student Management System |
| 📘 **Practical** | 7 |
| 🐍 **Programming Language** | Python |
| 🌐 **Framework** | Flask |
| 🗄️ **Database** | SQLite |
| 🎨 **Frontend** | HTML5 |
| 🧩 **Template Engine** | Jinja2 |
| 🔄 **Database Operations** | CRUD |
| 🔧 **Version Control** | Git |
| 🐙 **Repository Hosting** | GitHub |

---

<div align="center">

### 🎓 Practical 7 — Flask CRUD Application

**Built with Python • Flask • SQLite**

⭐ **Academic Project — Web Development Using Python**

</div>