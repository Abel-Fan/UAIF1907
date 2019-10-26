from flask import Blueprint,render_template,request,jsonify,make_response,session,redirect
from util.myutil import islogin
from flask_login import login_user,UserMixin,login_required,logout_user
from database.db import session
from database.tables import Admins,Teachers,Students
# 创建登录用户
class User(UserMixin):
    pass


index = Blueprint("index",__name__,url_prefix="/")

@index.route("/")
# @islogin
@login_required
def indexs():
    return render_template("index/index.html")

@index.route("/login",methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template("index/login.html")
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        type = request.form['type']
        if type=="0":
            # 教师
            pass
        elif type=="1":
            # 学生
            pass
        elif type=="2":
            # 管理员
            user1 = session.query(Admins).filter(Admins.username==username).one()
            if user1:
                if user1.password == password:
                    user = User()
                    user.id = username
                    login_user(user)
                    return jsonify({'code': 200, 'status': 'yes', 'msg': '管理员登录成功'})
                else:
                    return jsonify({'code': 200, 'status': 'no', 'msg': '密码错误'})

        # 比对数据库

        return jsonify({'code':200,'status':'no','msg':'用户不存在'})

@index.route("/loginout")
def loginout():
    logout_user()
    return redirect("/login")