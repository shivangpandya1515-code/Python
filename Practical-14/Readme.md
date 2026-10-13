# 🚀 Practical-14: Development of a RESTful Web API Using Django REST Framework (DRF)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-Framework-092E20?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST_Framework-API-red?logo=django&logoColor=white)
![Database](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## 📌 Experiment Title

**Development of a RESTful Web API Using Django REST Framework (DRF)**

## 🎯 Objective

To implement and understand REST API development using Django REST Framework by creating a Student Management API that supports Create, Read, Update, and Delete (CRUD) operations through HTTP requests and JSON data.

## 📖 Introduction

Django REST Framework (DRF) is a powerful toolkit built on Django for developing Web APIs. It provides serializers, views, routers, and a browsable API interface that simplify API development.

In this practical, a Student Management REST API is developed to manage student records. The API uses Django models to store data in an SQLite database and exposes endpoints that clients can access using standard HTTP methods.

## ✨ Features

- ➕ **Create:** Add new student records.
- 📋 **Read:** Retrieve all students or a specific student.
- ✏️ **Update:** Modify existing student information.
- 🗑️ **Delete:** Remove student records.
- 🔄 **RESTful Endpoints:** Use standard HTTP methods.
- 🔁 **Serialization:** Convert model instances to JSON-compatible data.
- ✅ **Data Validation:** Validate incoming API data.
- 🌐 **Browsable API:** Test endpoints through a web browser.
- 💾 **Database Integration:** Store student records using SQLite.

## 🧰 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Django | Web framework |
| Django REST Framework | REST API development |
| SQLite | Database |
| ModelSerializer | Serialization and validation |
| Visual Studio Code | Development environment |

## 📂 Project Structure

```text
Practical-14/
│
├── apiproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── .gitignore
├── manage.py
├── README.md
└── db.sqlite3
```

> **Note:** The `venv/` folder is omitted because it should not be uploaded to GitHub. The local database file is also excluded if your `.gitignore` contains `db.sqlite3`.

## ⚙️ Installation and Setup

### 1. Install Python

Check that Python is installed:

```bash
python --version
```

### 2. Create a Virtual Environment

Open the terminal inside the `Practical-14` folder and run:

```bash
python -m venv venv
```

Activate the environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell activation is blocked, you can run the environment's Python executable directly, as shown below.

### 3. Install Required Packages

```bash
python -m pip install django djangorestframework
```

If you need to install packages using the project's virtual environment explicitly on Windows:

```powershell
.\venv\Scripts\python.exe -m pip install django djangorestframework
```

Verify the installations:

```bash
python -m django --version
python -m pip show djangorestframework
```

### 4. Create the Django Project and App

If you are creating the project from scratch, run:

```bash
django-admin startproject apiproject .
python manage.py startapp students
```

Add `'rest_framework'` and `'students'` to `INSTALLED_APPS` in `apiproject/settings.py`.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'students',
]
```

## 🗃️ Database Model

File: `students/models.py`

```python
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name
```

The `Student` model contains three fields:

- `name`: Stores the student's name.
- `email`: Stores a unique email address.
- `course`: Stores the student's course.

Create and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 🔄 Creating the Serializer

File: `students/serializers.py`

```python
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
```

The `StudentSerializer` converts Student model instances into JSON-compatible representations and validates incoming data before it is saved.

Using `fields = '__all__'` includes all model fields, including the automatically generated ID.

## ⚡ Creating the API View

File: `students/views.py`

```python
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

The `ModelViewSet` provides standard CRUD actions:

- List student records.
- Retrieve a single student.
- Create a student.
- Update a student.
- Partially update a student.
- Delete a student.

## 🌐 URL Configuration

### Application URLs

File: `students/urls.py`

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet


router = DefaultRouter()
router.register('students', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]
```

The DRF router automatically generates the URL patterns for the Student API.

### Main Project URLs

File: `apiproject/urls.py`

```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('students.urls')),
]
```

The API endpoints are available under the `/api/` path.

## 📡 API Endpoints

The following endpoints are available when the server is running.

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/api/students/` | Retrieve all students |
| POST | `/api/students/` | Create a student |
| GET | `/api/students/1/` | Retrieve student with ID 1 |
| PUT | `/api/students/1/` | Replace student details |
| PATCH | `/api/students/1/` | Partially update student details |
| DELETE | `/api/students/1/` | Delete student with ID 1 |

**Note:** Replace `1` with the ID of an existing student when accessing an individual record.

## 🧪 Testing the API

### 1. Start the Development Server

```bash
python manage.py runserver
```

If your virtual environment is not activated on Windows, use:

```powershell
.\venv\Scripts\python.exe manage.py runserver
```

### 2. Open the Browsable API

Visit:

**http://127.0.0.1:8000/api/students/**

The Django REST Framework browsable API allows you to inspect responses and, where permitted, submit API requests through the browser.

### 3. Create a Student

Send a `POST` request to `/api/students/` with the following JSON:

```json
{
    "name": "Rahul Sharma",
    "email": "rahul@example.com",
    "course": "Computer Science"
}
```

Expected result: the API returns the created student record, normally with HTTP status `201 Created`.

### 4. Retrieve Students

Send a `GET` request to `/api/students/`.

Expected result: a JSON list of student records.

### 5. Update a Student

Send a `PUT` request to `/api/students/1/` with all required fields, or use `PATCH` to update only selected fields.

Expected result: the updated student record is returned.

### 6. Delete a Student

Send a `DELETE` request to `/api/students/1/`.

Expected result: the student record is removed, and a successful delete normally returns HTTP status `204 No Content`.

## 📊 Expected Results

| Operation | Expected Result |
|---|---|
| GET | Student records are retrieved |
| POST | A new student record is created |
| PUT | An existing record is replaced |
| PATCH | Selected fields are updated |
| DELETE | An existing record is deleted |
| Invalid data | Validation errors are returned |

## 🛡️ Important Notes

- Keep the `students/migrations/` files in your Git repository.
- Do not upload the virtual environment or secret environment variables.
- The default DRF configuration does not automatically provide user authentication or authorization. Configure suitable permissions and authentication before exposing sensitive data.
- The browsable API and endpoint behavior depend on the installed DRF version and project settings.

## 📈 Result

A RESTful Web API was developed using Django REST Framework to manage student records through Create, Read, Update, and Delete operations. The application demonstrates models, serializers, viewsets, routers, and JSON-based API communication.

## ✅ Conclusion

This practical provides an understanding of REST API development using Django REST Framework. It demonstrates how serializers, model viewsets, and routers simplify the development of reusable API endpoints and how clients can interact with database records using standard HTTP methods.

---

**Practical Number:** 14  
**Framework:** Django REST Framework  
**Database:** SQLite  
**Experiment:** Development of a RESTful Web API Using Django REST Framework (DRF)  
**Status:** Completed
