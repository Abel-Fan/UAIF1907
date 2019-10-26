from flask import Blueprint,render_template,request,jsonify
from database.db import session
from database.tables import Classes
from datetime import datetime
classes = Blueprint("classes",__name__,url_prefix="/classes")

@classes.route("/")
def index():
    return render_template("classes/index.html")

@classes.route("/add",methods=['POST'])
def add():
    username = request.form['username']
    if username:
        try:
            now = datetime.now()
            now = now.strftime("%Y-%m-%d %H:%M:%S")
            cls = Classes(username=username,utime=now,ctime=now)
            session.add(cls)
            session.commit()
        except BaseException as e:
            print("数据库异常",e)
            return jsonify({'code': 200, 'status': 'no', 'msg': '数据库异常请稍后重试'})

        return jsonify({'code':200,'status':'yes','msg':'添加成功'})
    else:
        return jsonify({'code':200,'status':'no','msg':'参数不正确'})


