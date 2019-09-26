from socket import socket
import requests
import lxml.etree as etree
url = "http://m.youdao.com/translate"

def fanyi(con):
    res = requests.post(url=url,data={
        'inputtext':con,
        'type':'AUTO'
    },headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Referer':'http://fanyi.youdao.com/'
    })
    htmlobj = etree.HTML(res.text)
    res = htmlobj.xpath("//ul[@id='translateResult']/li/text()")[0]
    return res


s = socket()
address = ('192.168.1.123',8080)
print("服务器绑定address(%s:%s)"%address)
s.bind(address)
s.listen(5)
print("服务器建立监听")
while True:
    c,address = s.accept()
    print(address,"连接中")
    while True:
        con = c.recv(1024).decode()
        res = fanyi(con)
        c.send(res.encode())