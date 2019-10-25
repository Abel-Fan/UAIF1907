from flask import Flask
from myblueprints.studentblue import student
from myblueprints.teacher import teacher
from myblueprints.index import index
import os

app = Flask(__name__)
app.register_blueprint(student)
app.register_blueprint(teacher)
app.register_blueprint(index)
app.secret_key = os.urandom(16)
if __name__ == "__main__":
    app.run(debug=True)