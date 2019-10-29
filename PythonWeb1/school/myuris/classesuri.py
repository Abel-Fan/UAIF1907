from flask_restful import Resource,fields,marshal,reqparse
from flask import jsonify
from database.db import session
from database.tables import Classes as Cla
from datetime import datetime
import math


from database.tables import Admins,Teachers,Students,verify_auth_token
# flask-HTTPauth验证
from flask_httpauth import HTTPTokenAuth

auth = HTTPTokenAuth(scheme="JWT")

# 验证规则
# 从 requests  Authorization 获取 token ,并且 token的前缀 必须加  JWT
@auth.verify_token
def verify_token(token):  # 验证成功返回 True 验证失败返回False
    print('token',token)
    print(verify_auth_token(token))
    return verify_auth_token(token)







classes_fields = {
    'id':fields.Integer,
    'username':fields.String,
    'ctime':fields.Raw,
    'utime':fields.Raw
}

# 时间处理函数
def EditTime(item):
    item['ctime'] = item['ctime'].strftime("%Y-%m-%d %H:%M:%S")
    item['utime'] = item['utime'].strftime("%Y-%m-%d %H:%M:%S")
    return item

# 班级分页
class ClassesPage(Resource):
    @auth.login_required
    def get(self,page,limit):
        start = (page-1)*limit
        data = session.query(Cla).limit(limit).offset(start)
        arr = [ EditTime(marshal(item,classes_fields)) for item in data]
        num = session.query(Cla).count()
        pageNum =  math.ceil(num/limit)
        return {'code':200,'data':arr,'pagenum':pageNum}


# 获取班级列表信息
class ClassesList(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("username",type=str,required=True,help="username参数不正确")
        super().__init__()

    @auth.login_required
    def get(self):
        data = session.query(Cla).all()
        print(data)
        # 序列化
        arr = [ EditTime(marshal(item,classes_fields)) for item in data]
        # 时间处理
        return {'msg':'ok','data':arr},201

    # 添加
    def post(self):
        args = self.reqparse.parse_args()
        username = args.username
        now = datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        c = Cla(username=username,ctime=now,utime=now)
        session.add(c)
        session.commit()
        return {'msg':'ok','data':{'username':username,'ctime':now,'utime':now}}

# 获取班级单个信息
class Classes(Resource):
    def get(self,id):
        print(id)
        print("班级请求")
        return {'msg':'ok'},201
