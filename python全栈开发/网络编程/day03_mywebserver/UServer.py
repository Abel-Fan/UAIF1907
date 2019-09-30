"""
Userver 轻量级 web服务器框架

需求：
1、可以创建服务器
2、创建路由

"""
from socketserver import TCPServer,BaseRequestHandler
# 服务器 服务器处理程序

class UserverHandler(BaseRequestHandler):
    def handle(self):
        # 构造 request信息
        resCon = self.request.recv(1024)
        resText = resCon.decode('utf-8')

        resList = resText.split("\r\n")
        obj = {key: value for key, value in [tuple(item.split(": ")) for item in resList[1:] if item != ""]}
        info = resList[0].split()
        obj['method'], obj['url'], obj['protocol'] = info
        self.req = obj
        if 'favicon' in obj['url']:
            # login icon
            res = ("HTTP/1.1 201 OK\r\n\r\n" + "").encode('utf-8')
            self.request.sendall(res)
        elif 'static' in obj['url']:
            # 静态资源
            with open("."+obj['url'],'r',encoding='utf-8') as f:
                res = ("HTTP/1.1 201 OK\r\n\r\n" + f.read()).encode('utf-8')
                self.request.sendall(res)
        else:
            con = self.routes[obj['url']]()
            res = ("HTTP/1.1 201 OK\r\n\r\n"+con).encode('utf-8')
            self.request.sendall(res)

class Userver:

    def __init__(self):
        self.routes = {}


    def run(self,address):
        # 创建web服务器并且运行
        UserverHandler.routes = self.routes

        with TCPServer(address,UserverHandler) as s:
            s.serve_forever()

    def route(self,dirname):
        def routewrap(fun):
            self.routes[dirname] =fun
            return fun()
        return routewrap


def render(templateName):
    with open('templates/%s'%templateName,'r',encoding="utf-8") as f:
        return f.read()