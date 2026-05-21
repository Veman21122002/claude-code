from flask import Flask, render_template, request, session, redirect, url_for
import os
from functools import wraps

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-key-for-mock-auth")

USER_ID_KEY = "user_id"
USERNAME_KEY = "username"

@app.template_filter('currency')
def currency_filter(value):
    return f"₹{value:,.2f}"

@app.context_processor
def inject_user():
    return dict(current_user=session.get(USERNAME_KEY) if session.get(USER_ID_KEY) else None)

def login_user(user_id, username):
    session[USER_ID_KEY] = user_id
    session[USERNAME_KEY] = username

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if USER_ID_KEY not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function


# ------------------------------------------------------------------ #
# Routes                                                              #
# ------------------------------------------------------------------ #

@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_user(1, request.form.get("email"))
        return redirect(url_for("profile"))
    return render_template("login.html")


# ------------------------------------------------------------------ #
# Placeholder routes — students will implement these                  #
# ------------------------------------------------------------------ #

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("landing"))


@app.route("/profile")
@login_required
def profile():
    balance = 1250.50
    return render_template("profile.html", balance=balance, username=session.get(USERNAME_KEY))


@app.route("/expenses/add")
def add_expense():
    return "Add expense — coming in Step 7"


@app.route("/expenses/<int:id>/edit")
def edit_expense(id):
    return "Edit expense — coming in Step 8"


@app.route("/expenses/<int:id>/delete")
def delete_expense(id):
    return "Delete expense — coming in Step 9"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
