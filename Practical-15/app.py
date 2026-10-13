
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
