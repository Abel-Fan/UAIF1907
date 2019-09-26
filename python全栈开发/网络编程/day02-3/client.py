from socket import socket
import json

class Client:
    def __init__(self):
        self.__s_address = ('192.168.1.123',8000)
        self.__c = ""
        self.isLogin = False
    def createClinet(self):
        try:
            self.__c = socket()
            self.__c.connect(self.__s_address)
        except:
            print("连接失败")
            return
        while True:
            if not self.isLogin:
                self.login()
            return
    def login(self):
        while True:
            username = input("username:")
            password = input('password:')
            self.__c.send(
                json.dumps({'username':username,'password':password}).encode()
            )
            res = json.loads(self.__c.recv(1024).decode())
            if res['status']=="ok":
                self.isLogin = True
                print("登录成功")
                break

    def runftp(self):
        while True:
            input("")


if __name__ =="__main__":
    c = Client()
    c.createClinet()