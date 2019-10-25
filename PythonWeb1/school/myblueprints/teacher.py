from flask import Blueprint,render_template

teacher = Blueprint("teacher",__name__,url_prefix="/teacher")

@teacher.route("/")
def index():
    return render_template("teacher/index.html")

