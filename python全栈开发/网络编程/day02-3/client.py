from socket import socket
import json

class Client:
    def __init__(self):
        self.__s_address = ('127.0.0.1',8000)
        self.__c = ""
        self.isLogin = False
    def createClinet(self):
        try:
            self.__c = socket()
            self.__c.connect(self.__s_address)
        except:
            print("连接失败")
            return

        if not self.isLogin:
            self.login()
        self.runftp()


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
                self.username = username
                self.home = res['home']
                self.token =res['token']
                break

    def runftp(self):
        while True:
            con = input("%s@admin:%s >"%(self.username,self.home))
            self.send(con)
            con = self.recv()
            if con['status']=="quit":
                print("退出")
                self.isLogin=False
                break
            elif con['status']=="cd":
                self.home = con['con']
            else:
                print(con['con'])

    def send(self,con):
        self.__c.send( json.dumps({'con':con,'token':self.token}).encode())

    def recv(self):
        con = json.loads(self.__c.recv(1024).decode())
        return con


if __name__ =="__main__":
    c = Client()
    c.createClinet()