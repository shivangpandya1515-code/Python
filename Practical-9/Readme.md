# 🚀 Practical-9: Django Installation and Hello World Web Application

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Django-6.1.2-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/HTML-Response-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML"/>
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge" alt="Status"/>
</p>

## 📌 Experiment Details

| Field                    | Description                                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **Practical No.**        | 9                                                                                                          |
| **Experiment Title**     | Installation and Configuration of Django Framework with Development of a Basic Hello World Web Application |
| **Objective**            | To install and configure Django and develop a basic Hello World web application.                           |
| **Programming Language** | Python                                                                                                     |
| **Framework**            | Django                                                                                                     |
| **Application Type**     | Web Application                                                                                            |

---

## 🎯 Objective

To install and configure the Django framework and develop a basic Hello World web application. This practical aims to understand Django project creation, URL routing, views, HTTP responses, and the built-in development server.

## 📖 Introduction

Django is a high-level Python web framework used to develop secure and maintainable web applications. It follows the Model-View-Template (MVT) architectural pattern and provides built-in features for URL routing, database management, request handling, and administration.

In this practical, a basic Django project is created to display a Hello World message in a web browser. A view returns an HTTP response, and URL routing connects the home page to that view.

## ✨ Features

* 🐍 Python-based web development
* 🚀 Django project initialization
* 🌐 URL routing and request handling
* 👋 Hello World web page
* ⚡ Built-in development server
* 🗄️ Database initialization using migrations
* 🧪 Easy local testing through a web browser

## 🛠️ Technologies Used

| Technology    | Purpose                                       |
| ------------- | --------------------------------------------- |
| Python        | Core programming language                     |
| Django        | Web application framework                     |
| HTML          | Formats the response displayed in the browser |
| SQLite        | Default database for the Django project       |
| VS Code       | Code editor                                   |
| Google Chrome | Testing the web application                   |

## 📂 Project Structure

```text
Practical-9/
│
├── helloworld/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
│
├── venv/                 # Virtual environment (not committed)
├── .gitignore
├── db.sqlite3            # Local Django database
├── manage.py
└── README.md
```

**Note:** The `venv/` directory and `db.sqlite3` file may be excluded from Git using `.gitignore`. Django can recreate the database by applying migrations.

## ⚙️ Prerequisites

Before starting, ensure that the following software is installed:

* Python 3
* pip
* Visual Studio Code or another code editor
* A modern web browser

Verify Python:

```bash
python --version
```

Verify pip:

```bash
python -m pip --version
```

## 🚀 Installation and Setup

### 1️⃣ Create the project directory

```bash
mkdir Practical-9
cd Practical-9
```

If the directory already exists, open it in VS Code instead of creating it again.

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

Activate it using Windows Command Prompt:

```bat
venv\Scripts\activate
```

For Windows PowerShell:

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

Run this command inside `Practical-9`:

```bash
django-admin startproject helloworld .
```

The dot (`.`) creates the project in the current directory rather than adding another nested directory.

### 5️⃣ Create the Hello World view

Open `helloworld/views.py` and add:

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse(
        "<h1>Hello World!</h1><p>Welcome to Django.</p>"
    )
```

**Explanation:**

* `HttpResponse` sends a response to the browser.
* `home(request)` handles incoming requests to the home page.
* The HTML string displays the Hello World heading and welcome message.

### 6️⃣ Configure URL routing

Open `helloworld/urls.py` and use:

```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
]
```

**Explanation:**

* `path("", views.home, name="home")` maps the root URL to the `home` view.
* `path("admin/", admin.site.urls)` preserves Django's default admin route.

### 7️⃣ Apply database migrations

```bash
python manage.py migrate
```

This initializes the default Django database tables.

### 8️⃣ Run the development server

```bash
python manage.py runserver
```

The terminal should display a message similar to:

```text
Starting development server at http://127.0.0.1:8000/
```

### 9️⃣ Open the application

Visit the following URL in your browser:

**http://127.0.0.1:8000/**

## 🖥️ Expected Output

The browser should display:

# Hello World!

Welcome to Django.

The page confirms that the Django development server, home view, and URL routing are working correctly.

## 🧪 Testing

| Test Case          | Action                           | Expected Result                 |
| ------------------ | -------------------------------- | ------------------------------- |
| Home Page          | Open `/`                         | Displays Hello World            |
| URL Routing        | Visit the root URL               | Calls `views.home`              |
| Development Server | Run `python manage.py runserver` | Server starts on port 8000      |
| Database Setup     | Run `python manage.py migrate`   | Database migrations are applied |
| Unknown URL        | Visit an undefined route         | Django displays a 404 page      |

## 🔄 Application Workflow

```text
       ┌────────────────────┐
       │ Open Browser       │
       └─────────┬──────────┘
                 │
                 ▼
       ┌────────────────────┐
       │ Request Home URL   │
       │        /           │
       └─────────┬──────────┘
                 │
                 ▼
       ┌────────────────────┐
       │ Django URL Routing │
       └─────────┬──────────┘
                 │
                 ▼
       ┌────────────────────┐
       │ home(request) View │
       └─────────┬──────────┘
                 │
                 ▼
       ┌────────────────────┐
       │ HttpResponse       │
       └─────────┬──────────┘
                 │
                 ▼
       ┌────────────────────┐
       │ Display Hello World│
       └────────────────────┘
```

## 🏁 Result

The Django framework was successfully installed and configured. A basic Hello World web application was developed using a Django view and URL routing, and the application was executed successfully on the local development server.

## 📚 Conclusion

This practical introduced the fundamentals of Django web development. It demonstrated project creation, view implementation, URL configuration, database migration, and execution using the development server. These concepts provide a foundation for building more advanced Django applications.

## 👨‍💻 Author

**Student Name:** SHIVANG PANDYA<br>
**Practical Number:** 9<br>
**Subject:** Web Development Using Python

---

<p align="center">
  <b>🚀 Practical-9 | Django Hello World</b>
  <br/>
  <i>Building the foundation of web development with Python and Django.</i>
</p>
