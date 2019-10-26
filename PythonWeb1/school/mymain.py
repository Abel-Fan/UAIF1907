from flask import Flask,session
from myblueprints.studentblue import student
from myblueprints.teacher import teacher
from myblueprints.index import index,User
from myblueprints.classes import classes
import os
from flask_login import LoginManager,UserMixin



def createApp():
    # 实例化应用
    app = Flask(__name__)
    # 设置密钥
    app.secret_key = os.urandom(16)
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

    return app