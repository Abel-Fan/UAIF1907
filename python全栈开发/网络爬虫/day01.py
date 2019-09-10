from urllib.request import urlopen
import lxml.etree as et

url = "http://soso.huitu.com/search?kw=%E4%B8%AD%E7%A7%8B"
rep = urlopen(url)
# rep 类似于一个上下文管理器对象
res = rep.read().decode()
htmlobj = et.HTML(res)

arr = htmlobj.xpath("//div[@class='seozone']/a/img/@originalsrc")  # css img{}
# 下载
def upload(url):
    filename = "绘图网中秋图片/"+url.split("/")[-1]
    with open(filename,"wb") as f:
        f.write(urlopen(url).read())

for url in arr:
    upload(url)

