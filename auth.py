from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, UserMixin
from settings import SERVER_PASS

auth = Blueprint("auth", __name__)


class User(UserMixin):
    id = 1


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    if request.values.get("password") == SERVER_PASS:
        user = User()
        login_user(user)
        return redirect(url_for("main.server"))
    else:
        flash("Incorrect password")
        return redirect(url_for("auth.login"))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
