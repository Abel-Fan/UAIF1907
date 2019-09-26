from socket import socket
import json

class FTPserver:
    def __init__(self):
        self.__address = ('192.168.1.123',8000)
        self.__s = ""
        self.users=[
            {'username':'horns','password':'123456','home':r"C:\Users\yangd\Desktop\UIAIF1907\讲课内容\python全栈开发\网络编程\day02-3\root\horns"},
        ]
    def createServer(self):
        self.__s = socket()
        self.__s.bind(self.__address)
        self.__s.listen(10)
        print("服务器已开启，等待连接")
        while True:
            self.__c,self.__c_address = self.__s.accept()
            print(self.__c_address,"连接成功")


            self.login()



    def login(self):
        while True:
            obj = json.loads(self.__c.recv(1024).decode())
            print(obj)
            username = obj['username']
            password = obj['password']
            for user in self.users:
                if user['username']==username:
                    if user['password']==password:
                        res = {'status':'ok','msg':"登录成功",'home':user['home']}
                    else:
                        res = {'status':'error','msg':'密码错误'}
                else:
                    res = {'status':'error','msg':'用户名不存在'}

            if res['status'] != "ok":
                self.__c.send(json.dumps(res).encode())
            else:
                self.__c.send(json.dumps(res).encode())
                break




if __name__ == "__main__":
    ftp = FTPserver()
    ftp.createServer()


