import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from helpers import login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
# songs.db was downloaded from a source that got top 2000 songs of the last decade from spotify!
        #https://www.kaggle.com/datasets/paradisejoy/top-hits-spotify-from-20002019
db = SQL("sqlite:///songs.db")
users = SQL("sqlite:///users.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# The first page to be loaded when a user logs in is the homepage.
@app.route("/")
@login_required
def index():
    return render_template("index.html")


# Browse route leads to browse.html
@app.route("/browse")
@login_required
def browse():
    return render_template("browse.html")


# Select route leads to select.html. 4 rows are randomly selected from songs.db and sent to select.html to be displayed in a table.
@app.route("/select")
@login_required
def select():
    songs = db.execute("SELECT artist, song, danceability, energy, genre FROM songs ORDER BY RANDOM() LIMIT 4")

    return render_template("select.html", songs=songs)


# Login route prompts user for user code
@app.route("/login", methods=["GET", "POST"])
def login():
    # Forget any past users
    session.clear()

    # User reached route via POST
    if request.method == "POST":

        # Ensure code was entered
        if not request.form.get("code"):
            message = "Please enter a user code"
            return render_template("apology.html", message=message)

        # Query database for user code
        rows = users.execute("SELECT * FROM Users WHERE code = ?", request.form.get("code"))

        # Ensure code exists
        if len(rows) != 1:
            message = "This code does not exist"
            return render_template("apology.html", message=message)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET
    else:
        return render_template("login.html")


# Logout page redirects user back to login page
@app.route("/logout")
def logout():
    # Forget any user code
    session.clear()

    # Redirect user to login form
    return redirect("/")


# Rate route leads to rate.html
@app.route("/rate")
@login_required
def rate():
    return render_template("rate.html")


# Register route prompts user for a random code
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Access user input from form
        usercode = request.form.get("code")

        # Ensure that code exists
        if not usercode:
            message = "Please enter a code"
            return render_template("apology.html", message=message)

        # Add new users to users.db
        try:
            user_id = users.execute("INSERT into Users (code) VALUES (?)", usercode)
        except ValueError:
            message = "This code has already been used"
            return render_template("apology.html", message=message)

        # Remember login information
        session["user_id"] = user_id

        return redirect("/")

    # User accessed route via GET
    else:
        return render_template("register.html")



