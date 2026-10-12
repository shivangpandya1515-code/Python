# 🎓 Practical-13: Django CRUD Operations Using ModelForms

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-Framework-092E20?logo=django&logoColor=white)
![Database](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)
![CRUD](https://img.shields.io/badge/Operations-CRUD-success)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## 📌 Experiment Title

**Implementation of Create, Read, Update, and Delete (CRUD) Operations in Django Using ModelForms**

## 🎯 Objective

To implement and understand Django CRUD operations using ModelForms by developing a Student Management System that allows users to add, view, update, and delete student records.

## 📖 Introduction

Django is a high-level Python web framework used to develop secure and maintainable web applications. It provides an Object-Relational Mapper (ORM) for database operations and ModelForms for creating forms directly from database models.

This practical demonstrates the implementation of CRUD operations using Django ModelForms and SQLite. The application manages student information through a simple web interface.

## ✨ Features

- ➕ **Create:** Add new student records.
- 📋 **Read:** Display all student records in a table.
- ✏️ **Update:** Modify existing student information.
- 🗑️ **Delete:** Remove student records after confirmation.
- 📝 **ModelForms:** Generate form fields from the Student model.
- ✅ **Form Validation:** Validate submitted student information.
- 🛡️ **CSRF Protection:** Protect POST forms using Django's CSRF token.
- 💾 **Database Integration:** Store records using SQLite.

## 🧰 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Django | Web application framework |
| SQLite | Database |
| Django ModelForms | Form generation and validation |
| HTML | User interface |
| Visual Studio Code | Development environment |

## 📂 Project Structure

```text
Practical-13/
│
├── crudproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── templates/
│   │   └── students/
│   │       ├── student_list.html
│   │       ├── student_form.html
│   │       └── student_confirm_delete.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── .gitignore
├── manage.py
├── Readme.md
└── db.sqlite3
```

> **Note:** The `venv/` directory is excluded from this structure because it should not be uploaded to GitHub. The local database file is also excluded by the recommended `.gitignore`.

## ⚙️ Installation and Setup

### 1. Install Python

Make sure Python is installed on your computer.

Check the version:

```bash
python --version
```

### 2. Create a Virtual Environment

Open the terminal in the `Practical-13` folder and run:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install Django

```bash
python -m pip install django
```

Verify the installation:

```bash
python -m django --version
```

### 4. Create the Django Project and App

If you are creating the project from scratch, run:

```bash
django-admin startproject crudproject .
python manage.py startapp students
```

Add `'students'` to `INSTALLED_APPS` in `crudproject/settings.py`.

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
- `email`: Stores a valid, unique email address.
- `course`: Stores the student's course.

Create and apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 📝 Creating the ModelForm

File: `students/forms.py`

```python
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'course']
```

The `StudentForm` automatically generates form fields from the `Student` model and uses Django's built-in validation. The `save()` method can create a new record or save changes to an existing record.

## 🔄 CRUD Operations

### 1. Create — Add Student

The create view displays an empty form and saves a student when valid data is submitted.

```python
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(
        request,
        'students/student_form.html',
        {'form': form, 'title': 'Add Student'}
    )
```

### 2. Read — View Students

The list view retrieves all student records and displays them in a table.

```python
def student_list(request):
    students = Student.objects.all()
    return render(
        request,
        'students/student_list.html',
        {'students': students}
    )
```

### 3. Update — Edit Student

The update view loads the existing student and passes it to the ModelForm through `instance=student`.

```python
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(
        request,
        'students/student_form.html',
        {'form': form, 'title': 'Update Student'}
    )
```

### 4. Delete — Remove Student

The delete view asks for confirmation and deletes the student only after a POST request.

```python
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(
        request,
        'students/student_confirm_delete.html',
        {'student': student}
    )
```

> **Note:** These snippets illustrate the individual operations. The complete implementations are in `students/views.py`, along with the necessary imports.

## 🌐 URL Configuration

File: `students/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.student_create, name='student_create'),
    path('edit/<int:pk>/', views.student_update, name='student_update'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),
]
```

File: `crudproject/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
]
```

## 🖥️ HTML Templates

The application uses three HTML templates inside `students/templates/students/`.

| Template | Purpose |
|---|---|
| `student_list.html` | Displays all students and CRUD action links |
| `student_form.html` | Adds or updates student information |
| `student_confirm_delete.html` | Confirms deletion before removing a record |

The form template uses `{{ form.as_p }}` to display the ModelForm fields and `{% csrf_token %}` to include Django's CSRF token.

## ▶️ Running the Application

### Step 1: Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 2: Start the Development Server

```bash
python manage.py runserver
```

### Step 3: Open the Application

Visit the following URL in your web browser:

**http://127.0.0.1:8000/**

### Step 4: Test CRUD Operations

1. Click **Add Student** and enter student details.
2. Verify that the new student appears in the table.
3. Click **Edit** to modify the student's information.
4. Click **Delete** and confirm the deletion.
5. Verify that the deleted student is no longer displayed.

## 🧪 Testing and Expected Results

| Test Case | Expected Result |
|---|---|
| Add a student with valid data | Student record is created |
| Open the home page | Student records are displayed |
| Submit an invalid email | Form validation displays an error |
| Add an email that already exists | Unique constraint validation prevents duplication |
| Update a student | Changes are saved to the database |
| Delete a student | Record is removed after confirmation |
| Submit a form without a valid CSRF token | Django rejects the request |

## 🛡️ Important Concepts

- **Django Model:** Defines the structure of student records.
- **ModelForm:** Generates form fields and validates submitted data.
- **Django ORM:** Performs database operations through Python objects.
- **URL Routing:** Maps browser URLs to the appropriate views.
- **Templates:** Render the application's HTML pages.
- **CSRF Protection:** Helps protect POST requests against forged submissions.
- **SQLite:** Stores the student records in a local database.

## 📊 Result

The Django application was implemented to perform Create, Read, Update, and Delete operations on student records using ModelForms and SQLite.

## ✅ Conclusion

This practical demonstrates the use of Django ModelForms for efficient form handling and validation, along with Django ORM for database operations. The Student Management System provides a practical understanding of CRUD functionality, URL routing, templates, and database integration in Django.

---

**Practical Number:** 13  
**Framework:** Django  
**Database:** SQLite  
**Experiment:** Django CRUD Operations Using ModelForms  
**Status:** Completed
