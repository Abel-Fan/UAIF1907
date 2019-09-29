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
        resText = self.request.recv(1024).decode('utf-8')
        resList = resText.split("\r\n")
        obj = {key: value for key, value in [tuple(item.split(": ")) for item in resList[1:] if item != ""]}
        info = resList[0].split()
        obj['method'], obj['url'], obj['protocol'] = info
        self.req = obj
        con = self.routes[obj['url']]()
        self.request.sendall(("HTTP/1.1 201 OK\r\n\r\nAccept-Language: zh-CN,zh;q=0.9\r\n "+con).encode('utf-8'))



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
