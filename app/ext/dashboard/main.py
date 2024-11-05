from flask import Blueprint, render_template


index = Blueprint("dashboard", __name__, template_folder="templates")

@index.route("/")
def dashboard():
    return render_template("index.html")