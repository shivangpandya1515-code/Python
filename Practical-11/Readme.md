# 🛡️ Practical-11: Django Admin Panel Configuration and Utilization

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Django-Framework-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
  <img src="https://img.shields.io/badge/Admin-Panel-blue?style=for-the-badge" alt="Admin Panel"/>
</p>

## 📌 Experiment Details

| Field | Description |
|---|---|
| **Practical Number** | 11 |
| **Experiment Title** | Configuration and Utilization of the Django Admin Panel for Web Application Data Management |
| **Objective** | To implement and understand the Django Admin Panel. |
| **Programming Language** | Python |
| **Framework** | Django |
| **Database** | SQLite |
| **Application** | Student Management System |

---

## 🎯 Objective

To configure and utilize the Django Admin Panel for web application data management. This practical demonstrates how to register models, create an administrator account, access the administration interface, and perform database operations through the built-in Django Admin Panel.

## 📖 Introduction

Django Admin is a built-in administration interface that allows authorized users to manage application data without creating a separate management interface.

In this practical, a Student Management System is developed using Django. A Student model is registered with the Admin Panel, allowing an administrator to add, view, update, search, filter, and delete student records stored in an SQLite database.

## ✨ Features

- 🔐 Administrator authentication
- 🎓 Student record management
- ➕ Add new student records
- 📋 View existing records
- ✏️ Update student information
- 🗑️ Delete student records
- 🔍 Search students by name, email, or course
- 🗂️ Filter student records by course
- 🗄️ SQLite database integration

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Django | Web framework |
| Django Admin | Administrative interface |
| SQLite | Database storage |
| Django ORM | Database operations |
| Visual Studio Code | Code editor |
| Web Browser | Accessing the Admin Panel |

## 📂 Project Structure

```text
Practical-11/
│
├── adminproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── venv/                 # Virtual environment (excluded from Git)
├── .gitignore
├── db.sqlite3            # Local database (optional to exclude)
├── manage.py
└── README.md
```

## ⚙️ Prerequisites

Ensure that the following software is installed:

- Python 3
- pip
- Django
- Visual Studio Code
- A modern web browser

Check your Python installation:

```bash
python --version
```

## 🚀 Installation and Setup

### 1️⃣ Create the project directory

```bash
mkdir Practical-11
cd Practical-11
```

If the folder already exists, open it in VS Code instead.

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

Activate it in Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3️⃣ Install Django

```bash
python -m pip install django
```

Verify the installed version:

```bash
python -m django --version
```

### 4️⃣ Create the Django project

```bash
django-admin startproject adminproject .
```

The dot (`.`) creates the project in the current directory.

### 5️⃣ Create the students application

```bash
python manage.py startapp students
```

### 6️⃣ Register the application

Open `adminproject/settings.py` and add `'students',` to `INSTALLED_APPS`.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'students',
]
```

## 🧱 Student Model Implementation

Open `students/models.py` and define the Student model:

```python
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name
```

### Model Fields

| Field | Description |
|---|---|
| `id` | Automatically generated primary key |
| `name` | Stores the student's name |
| `email` | Stores a unique email address |
| `course` | Stores the student's course |

## 🗄️ Database Configuration

Generate the migration files:

```bash
python manage.py makemigrations
```

Apply the migrations:

```bash
python manage.py migrate
```

Django creates the necessary database tables in `db.sqlite3`.

## 🛠️ Django Admin Configuration

Open `students/admin.py` and add the following code:

```python
from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'course')
    search_fields = ('name', 'email', 'course')
    list_filter = ('course',)
```

### Explanation

- `@admin.register(Student)` registers the Student model in Django Admin.
- `list_display` specifies the columns shown in the student list.
- `search_fields` enables searching by name, email, and course.
- `list_filter` provides a filter for student courses.

## 👤 Create a Superuser

Run the following command:

```bash
python manage.py createsuperuser
```

Enter a username, email address, and password when prompted.

The superuser account provides administrative access to the Django Admin Panel.

## ▶️ Run the Application

Start the development server:

```bash
python manage.py runserver
```

Open the following address in your browser:

**Admin Panel:** http://127.0.0.1:8000/admin/

Log in using the superuser credentials you created.

## 📋 Using the Django Admin Panel

After logging in, follow these steps:

1. Open the **Students** section.
2. Click **Add Student** to create a new record.
3. Enter the student's name, email address, and course.
4. Click **Save** to store the record.
5. Select an existing record to edit its information.
6. Use the delete option to remove a record.
7. Use the search box to find students.
8. Use the course filter to narrow the displayed records.

## 🧪 Testing

| Test Case | Expected Result |
|---|---|
| Open the Admin Panel | Login page is displayed |
| Enter valid administrator credentials | Admin dashboard opens |
| Add a student | Student record is saved |
| View student records | Registered student entries appear |
| Edit a student | Updated information is saved |
| Delete a student | Selected record is removed after confirmation |
| Search by name or email | Matching records are displayed |
| Filter by course | Records are filtered by the selected course |

## 🏁 Result

The Django Admin Panel was configured and utilized successfully. The Student model was registered, an administrator account was created, and student records could be managed through the built-in administration interface.

## 📚 Conclusion

This practical demonstrates how Django Admin simplifies web application data management. By registering models and configuring administrative options, database records can be created, viewed, updated, searched, filtered, and deleted without building a separate administration interface.

## 👨‍💻 Author

**Student Name:** Shivang Pandya  
**Practical Number:** 11  
**Subject:** Web Development Using Python

---

<p align="center">
  <b>🛡️ Practical-11 | Django Admin Panel</b>
  <br/>
  <i>Efficient application data management with Django.</i>
</p>
