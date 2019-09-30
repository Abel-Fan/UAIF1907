"""
myserver 网站后台
"""
from UServer import Userver,render
import pickle

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

@app.route("/")
def index():
    # 读取数据库数据
    with open("a.txt","rb") as f:
        obj = pickle.load(f)
    return render("index.html",**obj)



if __name__ =="__main__":
    app.run(address = ('192.168.1.234',8000))