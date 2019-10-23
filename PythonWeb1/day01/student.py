# step1 导入蓝图
from flask import Blueprint,request,render_template,redirect
# step2 创建蓝图
student = Blueprint('student',__name__,url_prefix="/student",static_folder="./static")
# 学生管理模块

# 连接数据库
import pymysql

# 连接数据库
db = pymysql.connect(database="deme1",user='root',password='123456',host='127.0.0.1',port=3306)
cursor = db.cursor()
# 创建路由
@student.route("/")
def index():   # 视图函数
    # 创建游标

    sql = "select * from student"
    cursor.execute(sql)
    data = cursor.fetchall()
    return render_template("student.html",data=data)

@student.route("/add",methods=['GET','POST'])
def add():
    if request.method == "GET":
        return render_template("addStudent.html")
    else:
        form = request.form
        sql = "insert into student (num,username,age,sex,class) values ('%s','%s',%s,%s,'%s') "%(form['num'],form['name'],form['age'],form['sex'],form['class'])
        cursor.execute(sql)
        db.commit()
        return redirect("/student")

@student.route("/del/<id>",methods=['GET'])
def delstu(id):
    sql = 'delete from student where id=%s'%id
    # 删除
    cursor.execute(sql)
    # 更新数据库
    db.commit()
    return redirect("/student/")

@student.route("/edit",methods=['POST'])
def edit():
    sql = "update student set username='%s',num='%s',age=%s,sex=%s,class='%s' where id=%s"%(request.form['name'],request.form['num'],request.form['age'],request.form['sex'],request.form['class'],request.form['id'])
    cursor.execute(sql)
    db.commit()
    return "ok"

