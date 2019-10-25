from flask import Blueprint,render_template,request,jsonify,make_response,session,redirect
from util.myutil import islogin

index = Blueprint("index",__name__,url_prefix="/")

@index.route("/")
@islogin
def indexs():
    return render_template("index/index.html")

@index.route("/login",methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template("index/login.html")
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        # 比对数据库
        if username =="admin" and password == "123456":
            resp = make_response(jsonify({'code':200,'status':'yes','msg':'登录成功'}))
            # resp.set_cookie("isLogin",'yes',max_age=10*60)
            session['username'] = 'admin'
            return resp
        else:
            return jsonify({'code':200,'status':'no','msg':'登录失败'})

@index.route("/loginout")
def loginout():
    print(session.get("username"))
    session.pop('username')
    return redirect("/login")