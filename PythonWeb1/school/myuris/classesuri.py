from flask_restful import Resource,fields,marshal
from flask import jsonify
from database.db import session
from database.tables import Classes as Cla


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


# 获取班级列表信息
class ClassesList(Resource):
    def get(self):
        data = session.query(Cla).all()
        print(data)
        # 序列化
        arr = [ EditTime(marshal(item,classes_fields)) for item in data]
        # 时间处理

        return {'msg':'ok','data':arr},201

# 获取班级单个信息
class Classes(Resource):
    def get(self,id):
        print(id)
        print("班级请求")
        return {'msg':'ok'},201
