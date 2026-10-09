
from flask import Flask, request, redirect, url_for, session

app = Flask(__name__)

# Secret key for session management
app.secret_key = "change-this-to-a-random-secret-key"

# Demo user credentials
USERNAME = "admin"
PASSWORD = "admin123"


@app.route("/", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if username == USERNAME and password == PASSWORD:
            session.clear()
            session["username"] = username
            return redirect(url_for("dashboard"))
        else:
            message = "Invalid username or password!"

    return f"""
    <h2>User Login</h2>
    <form method="POST">
        <label>Username:</label>
        <input type="text" name="username" required>
        <br><br>

        <label>Password:</label>
        <input type="password" name="password" required>
        <br><br>

        <button type="submit">Login</button>
    </form>
    <p>{message}</p>
    """


@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))

    username = session["username"]

    return f"""
    <h2>Welcome, {username}!</h2>
    <p>You are successfully logged in.</p>
    <a href="/logout">Logout</a>
    """


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)