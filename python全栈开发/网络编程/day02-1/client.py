from socket import socket

c = socket()
s_address = ('192.168.179.65',8888)
try:
    c.connect(s_address)
    c.send("杨登辉".encode())
    res = c.recv(1024)
    print(res)
except:
    print("链接失败")