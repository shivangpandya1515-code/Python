# 🎓 Practical-10: Django Models and Database Integration

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Django-ORM-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge" alt="Status"/>
</p>

## 📌 Experiment Details

| Field                    | Description                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------- |
| **Practical Number**     | 10                                                                                           |
| **Experiment Title**     | Implementation of Django Models and Database Integration for Web Application Data Management |
| **Objective**            | To implement and understand Django models and database integration.                          |
| **Programming Language** | Python                                                                                       |
| **Framework**            | Django                                                                                       |
| **Database**             | SQLite                                                                                       |
| **Application**          | Student Management System                                                                    |

## 🎯 Objective

To implement and understand Django models and database integration for web application data management. This practical demonstrates how to define database models, create database tables using migrations, insert and retrieve records, and display student information using Django.

## 📖 Introduction

Django is a Python web framework that provides an Object-Relational Mapper (ORM) for interacting with databases using Python classes and objects.

In this practical, a Student Management System is developed using Django models and SQLite. Student details are stored in a database and displayed on a web page. The Django Admin panel is used to manage student records.

## ✨ Features

* 🎓 Student model for managing student information
* 🗄️ SQLite database integration
* 🔄 Database migrations
* ➕ Add student records through Django Admin
* 📋 Retrieve and display student records
* 🌐 Browser-based student listing page
* 🛠️ Django ORM for database operations

## 🛠️ Technologies Used

| Technology | Purpose                    |
| ---------- | -------------------------- |
| Python     | Programming language       |
| Django     | Web application framework  |
| SQLite     | Database management        |
| Django ORM | Database operations        |
| HTML       | Displaying student records |
| VS Code    | Development environment    |

## 📂 Project Structure

```text
Practical-10/
│
├── studentproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── templates/
│   │   └── students/
│   │       └── student_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── venv/
├── .gitignore
├── db.sqlite3
├── manage.py
└── README.md
```

## ⚙️ Prerequisites

* Python 3
* pip
* Django
* Visual Studio Code
* A modern web browser

## 🚀 Installation and Setup

### 1. Create the project directory

```bash
mkdir Practical-10
cd Practical-10
```

If the folder already exists, open it in VS Code instead.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Django

```bash
python -m pip install django
```

Verify the installation:

```bash
python -m django --version
```

### 4. Create the Django project

```bash
django-admin startproject studentproject .
```

### 5. Create the students application

```bash
python manage.py startapp students
```

Add `'students',` to `INSTALLED_APPS` in `studentproject/settings.py`.

## 🧱 Model Implementation

The Student model is defined in `students/models.py`.

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

| Field    | Description                         |
| -------- | ----------------------------------- |
| `name`   | Stores the student's name           |
| `email`  | Stores a unique email address       |
| `course` | Stores the course name              |
| `id`     | Automatically generated primary key |

## 🔄 Database Migration

Generate the migration file:

```bash
python manage.py makemigrations students
```

Apply migrations to the database:

```bash
python manage.py migrate
```

Django creates the database table for the Student model in the SQLite database.

## 🛠️ Django Admin Configuration

In `students/admin.py`, register the model:

```python
from django.contrib import admin
from .models import Student

admin.site.register(Student)
```

Create an administrator account:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

Open the Django Admin panel:

**http://127.0.0.1:8000/admin/**

Log in and add student records through the Students section.

## 🌐 Display Student Records

The `student_list` view in `students/views.py` retrieves student records:

```python
from django.shortcuts import render
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(
        request,
        "students/student_list.html",
        {"students": students}
    )
```

The HTML template at `students/templates/students/student_list.html` displays the records in a table.

Configure `students/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_list, name="student_list"),
]
```

Include the app URLs in `studentproject/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("students.urls")),
]
```

## ▶️ Run the Application

Execute:

```bash
python manage.py runserver
```

Visit the student listing page:

**http://127.0.0.1:8000/**

To add records, open:

**http://127.0.0.1:8000/admin/**

## 🧪 Testing

| Test Case                          | Expected Result                    |
| ---------------------------------- | ---------------------------------- |
| Run migrations                     | Student database table is created  |
| Open Django Admin                  | Admin login page appears           |
| Add a student                      | Student record is saved            |
| Open the home page                 | Student records appear in a table  |
| Add multiple students              | All saved records are displayed    |
| Open the home page with no records | “No student records found” appears |

## 🧠 Key Concepts Learned

* Django models and model fields
* Database integration using SQLite
* Django Object-Relational Mapper (ORM)
* Database migrations
* Django Admin registration
* Retrieving records using `Student.objects.all()`
* URL routing and views
* Rendering database records in HTML templates

## 🏁 Result

Django models and database integration were implemented using SQLite. A Student model was created, migrations were applied, and student records were added through Django Admin and displayed on a web page.

## 📚 Conclusion

This practical demonstrates how Django models define database structures and how Django ORM simplifies database operations. The application provides a foundation for developing database-driven web applications.

## 👨‍💻 Author

**Student Name:** SHIVANG PANDYA<br>
**Practical Number:** 10<br>
**Subject:** Web Development Using Python

---

<p align="center">
  <b>🎓 Practical-10 | Django Models and Database Integration</b>
  <br/>
  <i>Learning database-driven web development with Django.</i>
</p>
