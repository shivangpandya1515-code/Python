from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = "database.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            course TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# READ
@app.route("/")
def index():

    conn = get_db_connection()

    students = conn.execute(
        "SELECT * FROM students"
    ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        students=students
    )


# CREATE
@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]

        conn = get_db_connection()

        conn.execute(
            """
            INSERT INTO students
            (name, email, course)
            VALUES (?, ?, ?)
            """,
            (name, email, course)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    return render_template("add.html")


# UPDATE
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    conn = get_db_connection()

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?",
        (id,)
    ).fetchone()

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]

        conn.execute(
            """
            UPDATE students
            SET name = ?, email = ?, course = ?
            WHERE id = ?
            """,
            (name, email, course, id)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    conn.close()

    return render_template(
        "edit.html",
        student=student
    )


# DELETE
@app.route("/delete/<int:id>")
def delete(id):

    conn = get_db_connection()

    conn.execute(
        "DELETE FROM students WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("index"))


if __name__ == "__main__":

    init_db()

    app.run(debug=True)