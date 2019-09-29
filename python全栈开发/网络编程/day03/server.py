from socket import socket,AF_INET,SOCK_DGRAM

s = socket(AF_INET,SOCK_DGRAM)

address = ('192.168.1.192',8000)
s.bind(address)

while True:

    con,c_addresss = s.recvfrom(1024)
    print(con,c_addresss)
    s.sendto("hi".encode(),c_addresss)
