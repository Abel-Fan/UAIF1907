from socket import socket
client = socket()

try:
    client.connect(('192.168.1.10',8000))
except:
    print("链接失败")
