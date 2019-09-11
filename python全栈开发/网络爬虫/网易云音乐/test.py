# URL = "https://music.163.com/artist?id=3684"
# URL2 = 'https://music.163.com/song/media/outer/url?id='

# 412911436

from urllib.request import urlopen
import lxml.etree as etree
import time

URL = "https://music.163.com/artist?id=7763"

con = urlopen(URL).read().decode()
htmlObj = etree.HTML(con)

arr = htmlObj.xpath("//ul[@class='f-hide']/li/a/@href")
filenames = htmlObj.xpath("//ul[@class='f-hide']/li/a/text()")
ids = [ i[9:] for i in arr]
data = zip(filenames,ids)

def upload(filename,idnum):
    data = urlopen('https://music.163.com/song/media/outer/url?id=%s'%idnum).read()
    with open("songs/%s.mp3"%filename,"wb") as f:
        f.write(data)
    print("歌曲《%s》下载完成"%filename)
    time.sleep(5)

for filename,idnum in data:
    upload(filename,idnum)