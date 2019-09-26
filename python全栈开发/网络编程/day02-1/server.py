from socket import socket,AF_INET,SOCK_STREAM
import time
# 时间服务器 返回北京时间

s = socket(AF_INET,SOCK_STREAM)
# 服务器绑定地址
address1 = ('192.168.1.123',8888)
s.bind( address1 )
# 开始监听
s.listen(5)
print("监听中..")
print("等待链接")
# 阻塞
while True:
    c,address = s.accept()
    print(address,"链接成功")
    try:
        print("name:",c.recv(1024).decode())
    except:
        print("error")
        c.close()
        c.send(
            ("%s:%s  %s"%(address1[0],address1[1],time.strftime("%Y-%m-%d %H:%M:%S"))).encode()
        )


