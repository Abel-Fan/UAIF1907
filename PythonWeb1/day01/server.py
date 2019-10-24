from flask import Flask,render_template,request,redirect,Blueprint,abort,jsonify
from db.database import Base,engine,session
from db.tables import Student

# 导入student蓝图
from student import student

# 实例化web应用  web服务器
app = Flask(__name__)

app.register_blueprint(student)

@app.route("/")
def index():
    data = session.query(Student).all()
    # 把对象转化为序列

    return jsonify(data)



if __name__ == "__main__":
    app.run(debug=True,port=8000)
    Base.metadata.create_all(engine)
