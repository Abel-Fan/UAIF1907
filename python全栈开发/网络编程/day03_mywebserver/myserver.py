"""
myserver 网站后台
"""
from UServer import Userver

# 实例化应用

app = Userver()

@app.route('/')
def index():  # 视图函数 一定要又return
    return "<div>this is div</div>"

@app.route("/list")
def list():
    return "<div>list页面</div>"

@app.route("/con")
def con():
    return "这是详情页"



if __name__ =="__main__":
    app.run(address = ('192.168.1.238',8000))