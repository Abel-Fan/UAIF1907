from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/ydh/")
def ydh():
    return "<div style='width:200px;height:200px;border:1px solid red;'>hello world<div>"

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port="8888")