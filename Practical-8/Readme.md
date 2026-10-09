# 🔐 Practical-8: User Authentication and Login System Using Flask Sessions

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/Session-Authentication-success?style=for-the-badge&logo=letsencrypt&logoColor=white" alt="Session Authentication"/>
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge" alt="Project Status"/>
</p>

## 📌 Experiment Details

| Field                    | Description                                                                      |
| ------------------------ | -------------------------------------------------------------------------------- |
| **Practical No.**        | 8                                                                                |
| **Experiment Title**     | Implementation of a User Authentication and Login System in Flask Using Sessions |
| **Objective**            | To implement and understand user authentication and session management in Flask. |
| **Programming Language** | Python                                                                           |
| **Framework**            | Flask                                                                            |
| **Application Type**     | Web Application                                                                  |

---

## 🎯 Objective

To implement and understand a user authentication and login system using Flask sessions. This practical demonstrates how to validate user credentials, maintain a logged-in state, protect routes from unauthorized access, and securely log out a user by clearing session data.

## 📖 Introduction

User authentication is an essential component of web application security. It verifies the identity of a user before allowing access to restricted resources.

Flask provides session management that allows an application to maintain user-specific state across multiple HTTP requests. After successful authentication, the application stores the username in the session. Protected routes check this session before granting access.

This project demonstrates a basic login system with a dashboard and logout functionality using Python and Flask.

## ✨ Features

* 🔑 **User Login:** Accepts a username and password.
* ✅ **Credential Validation:** Checks the submitted credentials.
* 🪪 **Session Management:** Stores the authenticated username in a Flask session.
* 🛡️ **Protected Dashboard:** Restricts dashboard access to logged-in users.
* ❌ **Invalid Login Handling:** Displays an error for incorrect credentials.
* 🚪 **Logout Functionality:** Clears the session and redirects the user to the login page.
* 🌐 **Simple Web Interface:** Provides a browser-based login form.
* 🧪 **Easy Testing:** Supports testing of successful login, failed login, protected routes, and logout.

## 🛠️ Technologies Used

| Technology        | Purpose                                  |
| ----------------- | ---------------------------------------- |
| 🐍 Python         | Core programming language                |
| 🌶️ Flask         | Web application framework                |
| 🍪 Flask Sessions | Maintains the user's authenticated state |
| 🌐 HTML           | Creates the login interface              |
| 💻 VS Code        | Development environment                  |
| 🌍 Web Browser    | Runs and tests the application           |

## 📂 Project Structure

```text
Practical-8/
│
├── app.py          # Main Flask application
└── README.md       # Project documentation
```

## ⚙️ Prerequisites

Before running this project, ensure that you have installed:

* Python 3
* pip (Python package installer)
* Visual Studio Code or another code editor
* Google Chrome or any modern web browser

Verify your Python installation:

```bash
python --version
```

Verify pip:

```bash
python -m pip --version
```

## ▶️ How to Run the Application

Run the following command from the project directory:

```bash
python app.py
```

After the server starts, open this address in your browser:

**http://127.0.0.1:5000/**

Keep the terminal open while using the application.

## 🔐 Demo Login Credentials

The example application uses hard-coded credentials for educational purposes.

| Field    | Demo Value |
| -------- | ---------- |
| Username | `admin`    |
| Password | `admin123` |

> ⚠️ These credentials are for local testing only. A production application should use a database, securely hashed passwords, and appropriate security controls.

## 🧪 Testing the Application

### Test Case 1: Successful Login

1. Open the login page.
2. Enter the correct username and password.
3. Click the **Login** button.
4. Verify that the dashboard opens.

**Expected Result:** The user is redirected to the dashboard and a welcome message is displayed.

### Test Case 2: Invalid Credentials

1. Open the login page.
2. Enter an incorrect username or password.
3. Submit the form.

**Expected Result:** The message `Invalid username or password!` is displayed.

### Test Case 3: Protected Dashboard

1. Log out of the application.
2. Open `/dashboard` directly in the browser.

**Expected Result:** The application redirects the unauthenticated user to the login page.

### Test Case 4: Logout Functionality

1. Log in using the valid demo credentials.
2. Click the **Logout** link.
3. Attempt to access `/dashboard` again.

**Expected Result:** The session is cleared, and the user must log in again to access the dashboard.

## 🧠 Key Concepts Learned

| Concept            | Explanation                                                |
| ------------------ | ---------------------------------------------------------- |
| Flask Routing      | Maps URLs to Python functions.                             |
| HTTP Methods       | Uses GET to display pages and POST to submit credentials.  |
| Request Handling   | Reads submitted form data using `request.form`.            |
| Session Management | Maintains authentication state using `session`.            |
| Route Protection   | Checks whether a username exists in the session.           |
| URL Generation     | Uses `url_for()` to generate route URLs.                   |
| Logout             | Clears session data using `session.clear()`.               |
| Redirects          | Sends users to the appropriate page after login or logout. |

## 🔄 Application Workflow

```text
        ┌──────────────────┐
        │   Open Login     │
        │      Page        │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Enter Credentials│
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Validate Username│
        │    & Password    │
        └────────┬─────────┘
                 │
           ┌─────┴─────┐
           │           │
        Valid        Invalid
           │           │
           ▼           ▼
    ┌────────────┐ ┌──────────────┐
    │ Create     │ │ Display Error│
    │ Session    │ │   Message    │
    └─────┬──────┘ └──────────────┘
          │
          ▼
    ┌────────────┐
    │ Dashboard  │
    └─────┬──────┘
          │
          ▼
    ┌────────────┐
    │   Logout   │
    └─────┬──────┘
          │
          ▼
    ┌────────────┐
    │ Clear      │
    │ Session    │
    └────────────┘
```

## 🔒 Security Considerations

This project is intended for learning basic Flask session authentication. For real-world use:

* 🔐 Generate a strong, random secret key and keep it outside the source code.
* 🔑 Store passwords using a suitable password-hashing algorithm rather than plaintext.
* 🍪 Configure session cookies with `Secure`, `HttpOnly`, and appropriate `SameSite` settings for production.
* 🌐 Use HTTPS to protect data in transit.
* 🛡️ Disable Flask debug mode in production.
* 🗄️ Store user records in a database and implement proper authentication and authorization.
* 🚫 Add CSRF protection and login rate limiting where appropriate.

**Note:** Flask's default session is stored in a signed cookie. It is not an encrypted server-side session store, so sensitive information should not be placed directly in it.

## 🏁 Result

The user authentication and login system was implemented using Flask sessions. The application demonstrates credential validation, session creation, protection of restricted routes, and logout functionality.

## 📚 Conclusion

This practical provides a foundation for understanding authentication in Flask web applications. It explains how sessions maintain a user's login state and how protected routes and logout functionality can be implemented. These concepts can be extended to database-backed authentication systems and larger web applications.

## 👨‍💻 Author

**Student Name:** *SHIVANG PANDYA*<BR>
**Practical:** 8<BR>
**Subject:** Web Development / Python Programming

---

<p align="center">
  <b>🔐 Practical-8 | Flask Session-Based Authentication</b>
  <br/>
  <i>Learning web development one practical at a time.</i>
</p>
