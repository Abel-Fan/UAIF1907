from flask import Blueprint,render_template

student = Blueprint("student",__name__,url_prefix="/student")

@student.route("/")
def index():
    return render_template("student/index.html")

