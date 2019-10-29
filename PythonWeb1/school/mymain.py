from flask import Flask,session
from myblueprints.studentblue import student
from myblueprints.teacher import teacher
from myblueprints.index import index,User
from myblueprints.classes import classes
import os
from flask_login import LoginManager,UserMixin
from flask_restful import Api
from myuris.classesuri import Classes,ClassesList,ClassesPage

from database.tables import secret_key
import requests

def createApp():
    # 实例化应用
    app = Flask(__name__)
    # 设置密钥
    app.secret_key = secret_key
    # 加载蓝图
    app.register_blueprint(index)
    app.register_blueprint(student)
    app.register_blueprint(teacher)
    app.register_blueprint(classes)
    # 绑定 flask_login 插件
    login_manager = LoginManager(app)
    # login_manager配置信息
    login_manager.login_view = "/login"


    # 检测 会话 是否存在用户  是否登录
    @login_manager.user_loader
    def userLoader(username):
        # username  User.id
        if username:
            user= User()
            user.id = username
            return user


    # RestfulApi
    api = Api(app)

    # 注册接口 注册uri
    api.add_resource(Classes,'/api/classes/<int:id>',endpoint="classes")
    api.add_resource(ClassesList,'/api/classes/',endpoint="classeslist")
    api.add_resource(ClassesPage,'/api/classes/<int:page>/<int:limit>/',endpoint="classespage")
    return app