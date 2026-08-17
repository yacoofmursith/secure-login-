from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

# Find the templates folder correctly
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(__name__, template_folder=TEMPLATE_DIR)
app.secret_key = "change-this-secret-key"


def get_db():
    conn = sqlite3.connect(os.path.join(BASE_DIR, "users.db"))
    conn.row_factory = sqlite3.Row
    return conn


# Create database and users table
with get_db() as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)


@app.route("/")
def home():
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/login")


@app.route("/register", methods=["GET", "POST"])
def register():
    message = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        try:
            with get_db() as conn:
                conn.execute(
                    "INSERT INTO users (username, password) VALUES (?, ?)",
                    (username, hashed_password)
                )

            return redirect("/login")

        except sqlite3.IntegrityError:
            message = "Username already exists!"

    return render_template("register.html", message=message)


@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        with get_db() as conn:
            user = conn.execute(
                "SELECT * FROM users WHERE username = ?",
                (username,)
            ).fetchone()

        if user and check_password_hash(user["password"], password):
            session["user"] = username
            return redirect("/dashboard")

        message = "Invalid username or password!"

    return render_template("login.html", message=message)


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    return render_template(
        "dashboard.html",
        username=session["user"]
    )


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)