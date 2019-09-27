from socket import socket
import json,time,hashlib
import os

md5 = hashlib.md5()

class FTPserver:
    def __init__(self):
        self.__address = ('127.0.0.1',8000)
        self.__s = ""
        self.__root=r"C:\Users\yangd\Desktop\UIAIF1907\讲课内容\python全栈开发\网络编程\day02-3\root"
        self.users=[
            {'username':'horns','password':'123456','home':r"\horns"},
        ]
        self.tokens = []
    def createServer(self):
        self.__s = socket()
        self.__s.bind(self.__address)
        self.__s.listen(10)
        print("服务器已开启，等待连接")
        while True:
            self.__c,self.__c_address = self.__s.accept()
            print(self.__c_address,"连接成功")

            self.login()
            self.ftpserver()




    def login(self):
        while True:
            obj = json.loads(self.__c.recv(1024).decode())
            username = obj['username']
            password = obj['password']
            for user in self.users:
                if user['username']==username:
                    if user['password']==password:
                        token = str(int(time.time())).encode()
                        md5.update(token)
                        token = md5.hexdigest()
                        self.tokens.append(token)
                        res = {'status': 'ok', 'msg': "登录成功", 'home': user['home'],'token':token}
                        print(res)
                        os.chdir(self.__root+user['home'])
                    else:
                        res = {'status':'error','msg':'密码错误'}
                else:
                    res = {'status':'error','msg':'用户名不存在'}

            if res['status'] != "ok":
                self.__c.send(json.dumps(res).encode())
            else:
                self.__c.send(json.dumps(res).encode())
                break


    def ftpserver(self):
        while True:
            mls = self.recv().strip().split()
            print(mls)
            if mls[0]=="quit":
                print(self.__c_address,"退出")
                self.send({'status':'quit','con':""})
                self.__c.close()
                break
            elif mls[0] =="cd":
                pass
            elif mls[0] =="ls":
                con = "\n".join(os.listdir())
                self.send({'status':'ok','con':con})


    def recv(self):
        con = self.__c.recv(1024)
        con = json.loads(con.decode())
        if "token" in con:
            if con['token'] in self.tokens:
                return con['con']
        print(self.__c_address,"验证失败,强制退出")
        self.__c.close()

    def send(self,con):
        self.__c.send(json.dumps(con).encode())
if __name__ == "__main__":
    ftp = FTPserver()
    ftp.createServer()


