from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# DATABASE CONNECTION
def get_db_connection():

    conn = sqlite3.connect("school.db")
    conn.row_factory = sqlite3.Row

    return conn


# CREATE TABLE
def create_table():

    conn = get_db_connection()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS contacts(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT,
        message TEXT NOT NULL

    )
    """)

    conn.commit()
    conn.close()

create_table()


# HOME PAGE
@app.route("/")
def home():

    return render_template("home.html")


# ABOUT PAGE
@app.route("/about")
def about():

    return render_template("about.html")


# COURSES PAGE
@app.route("/courses")
def courses():

    return render_template("courses.html")


# CONTACT PAGE
@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        conn = get_db_connection()

        conn.execute("""
        INSERT INTO contacts(name, email, phone, message)
        VALUES (?, ?, ?, ?)
        """, (name, email, phone, message))

        conn.commit()
        conn.close()

        return """
        <h1 style='color:green;text-align:center;margin-top:100px;'>
        Message Sent Successfully
        </h1>
        """

    return render_template("contact.html")


# SERVER
if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )