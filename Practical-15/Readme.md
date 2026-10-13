# 🚀 Practical-15: Deployment and Configuration of a Flask Web Application on a Web Server

## 📌 Experiment Title
**Deployment and Configuration of a Flask or Django Web Application on a Web Server**

## 🎯 Objective
To implement and understand the deployment of a Flask/Django web application on a web server, including environment configuration, dependency management, and cloud deployment.

## 📖 Introduction
Flask is a lightweight Python web framework used to develop web applications. Deployment is the process of making an application available to users over the internet.

In this practical, a basic Flask web application is developed, tested locally, uploaded to GitHub, and configured for deployment using **Render** with **Gunicorn** as the production WSGI server.

## 🛠️ Technologies Used
- 🐍 **Python** – Programming language
- 🌶️ **Flask** – Web application framework
- 🦄 **Gunicorn** – WSGI HTTP server
- 🐙 **Git and GitHub** – Version control and source-code hosting
- ☁️ **Render** – Cloud deployment platform
- 💻 **Visual Studio Code** – Code editor

## 📂 Project Structure

```text
Practical-15/
├── venv/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

**File descriptions:**
- `app.py` – Contains the Flask application and home page.
- `requirements.txt` – Lists the Python packages required by the project.
- `.gitignore` – Prevents unnecessary files from being tracked by Git.
- `README.md` – Documents the experiment and deployment procedure.
- `venv/` – Local Python virtual environment; it should not be uploaded to GitHub.

## ⚙️ Step 1: Create the Project

Create a folder named `Practical-15` and open it in Visual Studio Code.

Open the terminal in that folder and create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

## 📦 Step 2: Install Required Packages

Install Flask and Gunicorn:

```bash
python -m pip install flask gunicorn
```

Generate the dependency file:

```bash
python -m pip freeze > requirements.txt
```

## 💻 Step 3: Develop the Flask Application

Create `app.py` and add the following code:

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Practical-15</title>
    </head>
    <body>
        <h1>Welcome to Practical-15!</h1>
        <p>My Flask application is running successfully.</p>
        <p>Deployment and configuration using Flask.</p>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
```

### 📝 Code Explanation

- `Flask(__name__)` initializes the Flask application.
- `@app.route("/")` defines the home page URL.
- `home()` returns the HTML content displayed in the browser.
- `app.run(debug=True)` starts the development server for local testing. Debug mode is intended for local development, not production deployment.
- Gunicorn serves the application in the Render deployment environment.

## 🧪 Step 4: Run the Application Locally

Run the following command:

```bash
python app.py
```

Open the following address in your web browser:

**http://127.0.0.1:5000/**

### ✅ Expected Output

The browser displays:

**Welcome to Practical-15!**

My Flask application is running successfully.

Deployment and configuration using Flask.

## 🗂️ Step 5: Configure `.gitignore`

Create a `.gitignore` file in the project root:

```gitignore
# Virtual environments
venv/
.venv/
env/

# Python cache
__pycache__/
*.py[cod]

# Environment variables
.env
.env.*

# IDE settings
.vscode/
.idea/

# Log files
*.log

# Operating system files
.DS_Store
Thumbs.db
```

This file prevents virtual environments, cache files, local environment variables, and unnecessary editor or operating-system files from being committed. Keep `requirements.txt` in Git because the deployment service needs it.

## 🐙 Step 6: Upload the Project to GitHub

Create a new repository on GitHub, then run these commands from the project folder:

```bash
git init
git add .
git commit -m "Add Practical-15 Flask deployment project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the URL of your own repository.

If Git is already initialized or the remote is already configured, skip the corresponding commands.

## ☁️ Step 7: Deploy the Application Using Render

1. Visit [Render](https://render.com/) and sign in.
2. Choose **New → Web Service**.
3. Connect your GitHub account and select the `Practical-15` repository.
4. Configure the service using the following settings:

| Configuration | Value |
|---|---|
| Runtime / Language | Python 3 |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app` |

5. Choose an available plan and create the web service.
6. Wait for the build and deployment process to complete.
7. Open the public URL provided by Render to access the deployed application.

**Important:** In `gunicorn app:app`, the first `app` refers to the `app.py` module, and the second `app` refers to the Flask application object inside that file.

For detailed instructions, refer to the [official Render Flask deployment guide](https://render.com/docs/deploy-flask).

## 🔍 Step 8: Test the Deployed Application

- Verify that the application runs locally.
- Open the public Render URL after deployment.
- Confirm that the home page displays the expected message.
- Refresh the page to verify that it responds correctly.
- If deployment fails, check the Render build and runtime logs for errors.

## 📊 Learning Outcomes

After completing this practical, students should understand:

- The basic process of developing a Flask web application.
- How to create and configure a Python virtual environment.
- How to manage project dependencies using `requirements.txt`.
- How to use Git and GitHub to store project source code.
- The role of Gunicorn in serving a Flask application in production.
- The basic process of deploying a web application to a cloud hosting platform.

## 🏁 Result

A basic Flask web application is developed and configured for deployment. After successfully completing the deployment steps, the application can be accessed through the public URL provided by Render.

## 🎓 Conclusion

This practical demonstrates the deployment and configuration of a Flask web application on a cloud web server. It covers application development, environment setup, dependency management, GitHub integration, and production serving with Gunicorn. Cloud deployment makes the application accessible through a public URL without requiring users to run it on their own computers.

---

**✨ Practical-15 | Python Web Development | Flask Application Deployment**