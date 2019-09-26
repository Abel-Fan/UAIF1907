from socket import socket

s = socket()
address = ('192.168.1.123',8080)
try:
    s.connect(address)
    print("欢迎使用有道翻译！！")
    while True:
        con = input("请输入内容：\n").encode()
        s.send(con)
        print(s.recv(1024).decode())
except:
    print("连接失败")