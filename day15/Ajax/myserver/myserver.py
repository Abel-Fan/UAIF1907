from flask import Flask,render_template,jsonify,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/ydh/")
def ydh():
    # return "<div style='width:200px;height:200px;border:1px solid red;'>hello world<div>"
    age = request.args.get("age")
    return jsonify({"name":"小白","age":age})

@app.route("/login",methods=["POST"])
def login():
    print("username",request.form.get("username"))
    print("password",request.form.get("passwrod"))
    return "ok"

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port="8888")