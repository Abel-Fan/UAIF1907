from flask import Flask,render_template,request,redirect,Blueprint

# 导入student蓝图
from student import student

# 实例化web应用  web服务器
app = Flask(__name__)

app.register_blueprint(student)



if __name__ == "__main__":
    app.run(debug=True,port=8000)
