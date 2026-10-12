# 🔐 Practical-12: Secure User Authentication in Django Using CSRF Protection

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-Framework-092E20?logo=django&logoColor=white)
![Authentication](https://img.shields.io/badge/Authentication-User%20Login-success)
![Security](https://img.shields.io/badge/Security-CSRF%20Protection-red)

## 📌 Experiment Title

**Implementation of Secure User Authentication in Django Using CSRF Protection**

## 🎯 Objective

To implement and understand Django user authentication with CSRF (Cross-Site Request Forgery) protection by developing a secure login system, restricting access to authenticated users, and providing logout functionality.

## 📖 Introduction

Django is a high-level Python web framework that provides built-in features for developing secure web applications.

This practical demonstrates Django's authentication system using its built-in authentication functions, sessions, middleware, and CSRF protection. Users can log in with valid credentials, access a protected dashboard, and log out securely.

### ✨ Key Features

- 🔑 User login using a username and password
- 🛡️ CSRF protection for POST forms
- 👤 Django's built-in user authentication
- 🔒 Protected dashboard for authenticated users
- 🚪 Logout functionality
- ⚠️ Error message for invalid login credentials
- 🗂️ Session-based authentication

## 🧰 Technologies Used

- **Programming Language:** Python
- **Web Framework:** Django
- **Frontend:** HTML
- **Authentication:** Django Authentication System
- **Security:** CSRF Middleware and CSRF Tokens
- **Database:** SQLite
- **Development Tool:** Visual Studio Code or any Python-compatible editor

## 📂 Project Structure

```text
Practical-12/
│
├── accounts/
│   ├── migrations/
│   ├── templates/
│   │   └── accounts/
│   │       ├── login.html
│   │       └── dashboard.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── authproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── .gitignore
├── manage.py
├── README.md
└── db.sqlite3
```

> **Note:** The `venv/` folder is excluded from the project structure because it should not be uploaded to GitHub. The local `db.sqlite3` database is also excluded when using the recommended `.gitignore`.

## ⚙️ Installation and Setup

### Step 1: Install Python

Ensure Python is installed on your system.

Check the installed version:

```bash
python --version
```

### Step 2: Open the Project Folder

Open the `Practical-12` folder in Visual Studio Code and open the integrated terminal.

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### Step 4: Install Django

```bash
python -m pip install django
```

Verify the installation:

```bash
python -m django --version
```

### Step 5: Create the Django Project and App

If you have not already created them, run:

```bash
django-admin startproject authproject .
python manage.py startapp accounts
```

Add `'accounts'` to `INSTALLED_APPS` in `authproject/settings.py`.

Ensure the default Django middleware includes:

```python
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
```

Keep Django's default middleware configuration and ordering intact.

## 🔑 Authentication Implementation

Django's built-in authentication functions are used to validate credentials, establish the user's session, and log out.

### 1. Login View

The login view accepts the username and password, authenticates the user, and redirects successful logins to the dashboard.

File: `accounts/views.py`

```python
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    error = ""

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        error = "Invalid username or password."

    return render(
        request,
        "accounts/login.html",
        {"error": error}
    )


@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")

    return redirect("dashboard")
```

### 2. Application URLs

File: `accounts/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_view, name="logout"),
]
```

### 3. Main Project URLs

File: `authproject/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
]
```

## 🖥️ Frontend Templates

### 1. Login Page

Create `accounts/templates/accounts/login.html`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django Secure Login</title>
</head>
<body>
    <h1>User Login</h1>

    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}

    <form method="POST">
        {% csrf_token %}

        <label>Username:</label>
        <input type="text" name="username" required>
        <br><br>

        <label>Password:</label>
        <input type="password" name="password" required>
        <br><br>

        <button type="submit">Login</button>
    </form>
</body>
</html>
```

**CSRF protection:** The `{% csrf_token %}` template tag adds a CSRF token to the form. Django's CSRF middleware validates the token on POST requests.

### 2. Dashboard Page

Create `accounts/templates/accounts/dashboard.html`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dashboard</title>
</head>
<body>
    <h1>Welcome, {{ request.user.username }}!</h1>

    <p>You are successfully logged in.</p>

    <form method="POST" action="{% url 'logout' %}">
        {% csrf_token %}
        <button type="submit">Logout</button>
    </form>
</body>
</html>
```

The `@login_required` decorator prevents unauthenticated users from accessing the dashboard. The logout form uses POST and includes a CSRF token.

## ▶️ Execution Steps

### Step 1: Apply Database Migrations

```bash
python manage.py migrate
```

### Step 2: Create a User Account

Create a superuser to use for login testing:

```bash
python manage.py createsuperuser
```

Follow the terminal prompts to set a username and password.

### Step 3: Start the Development Server

```bash
python manage.py runserver
```

### Step 4: Open the Application

Open this URL in your browser:

```text
http://127.0.0.1:8000/
```

Enter the username and password you created.

### Step 5: Test the Dashboard and Logout

- Log in using valid credentials.
- Verify that the dashboard displays the username.
- Click **Logout** to end the session.
- Try opening `/dashboard/` after logging out to verify that access is restricted.

## 🧪 Testing and Expected Results

| Test Case | Expected Result |
|---|---|
| Valid username and password | User is redirected to the dashboard |
| Invalid credentials | Error message is displayed |
| Anonymous user opens dashboard | User is redirected to the login page |
| POST request with a missing or invalid CSRF token | Django rejects the request |
| User submits the logout form | Session is logged out and login page opens |

## 🛡️ Security Features Explained

- **Authentication:** `authenticate()` verifies the submitted credentials.
- **Session management:** `login()` establishes an authenticated session and `logout()` ends it.
- **Access control:** `@login_required` restricts dashboard access.
- **CSRF protection:** Django's CSRF middleware and `{% csrf_token %}` protect POST forms against forged requests.
- **Password security:** Django stores user passwords using its password-hashing system rather than storing them as plain text.

> **Important:** For production deployment, also configure HTTPS, secure session and CSRF cookies, appropriate `DEBUG` and `ALLOWED_HOSTS` settings, and other deployment security settings.

## 📊 Result

The Django web application was successfully configured to demonstrate user authentication, session-based login and logout, protected dashboard access, and CSRF protection for POST forms.

## ✅ Conclusion

This practical demonstrates how Django's built-in authentication system and CSRF protection work together to support a more secure web application. It also provides an understanding of sessions, authentication middleware, protected routes, and form security.

## 👨‍💻 Author

**Student Name:** Shivang Pandya  
**Practical Number:** 12  
**Subject:** Web Development Using Python

---

<p align="center">
  <b>🛡️ Practical-12</b>
  <br/>
  <i>Secure User Authentication in Django Using CSRF Protection</i>
</p>