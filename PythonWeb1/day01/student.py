# step1 导入蓝图
from flask import Blueprint,request,render_template,redirect,jsonify
# step2 创建蓝图
student = Blueprint('student',__name__,url_prefix="/student",static_folder="./static")
# 学生管理模块

# 连接数据库
import pymysql

# 连接数据库
db = pymysql.connect(database="deme1",user='root',password='123456',host='127.0.0.1',port=3306)
cursor = db.cursor()
# 创建路由
@student.route("/",methods=["GET"])
def index():   # 视图函数
    # 创建游标
    return render_template("student.html")

# 返回学生资源
@student.route("/get",methods=['GET'])
def getStudent():
    sql = "select * from student"
    #  select 字段,.. from  表名 where 条件

    cursor.execute(sql)
    data = cursor.fetchall()
    return jsonify({'code':200,'data':data})

@student.route("/del",methods=['delete'])
def deleteStudent():
    id = request.form['id']
    # 判断id 是否存在
    try:
        sql = 'delete from student where id=%s'%id
        cursor.execute(sql)
        db.commit()
    except:
        return jsonify({'code':200,'status':'no','msg':'数据库异常,请稍后重试'})
    return jsonify({'code':200,'status':'yes','msg':"删除成功"})


@student.route("/add",methods=['GET',"POST"])
def addStudent():
    if request.method=="GET":
        return render_template("addStudent.html")
    elif request.method=="POST":
        # values
        # to_dict()

        # 做验证
        # 验证失败要有响应
        #return jsonify({'code': 200, 'status': 'error', 'msg': 'name不能为空'})
        data = request.form.to_dict()
        sql = 'insert into student (num,username,age,sex,class) values ("%s","%s",%s,%s,"%s")'%(data['num'],data['name'],data['age'],data['sex'],data['class'])
        try:
            cursor.execute(sql)
            db.commit()
        except:
            return jsonify({'code':200,'status':'error','msg':'数据库异常'})
        return jsonify({'code':200,'status':'yes','msg':'提交成功'})

