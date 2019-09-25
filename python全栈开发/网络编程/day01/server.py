import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
# 实例化 套接字对象
server.bind(('192.168.1.217',8000))  # 传入元组 address =  (ip,port)
server.listen(5)
while True:
    client,address = server.accept()
    print(address)
    client.close()



"""
地址簇
socket.AF_INET  ipv4(默认)
socket.AF_INET6 ipv6

协议
SOCK_STREAM TCP
SOCK_DGRAM UDP
"""