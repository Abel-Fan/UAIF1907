# URL = "https://music.163.com/artist?id=3684"
# URL2 = 'https://music.163.com/song/media/outer/url?id='

# 412911436

from urllib.request import urlopen,Request
import lxml.etree as etree
import time

URL = "https://music.163.com/artist?id=7763"
req = Request(URL,headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'referer':'https://music.163.com/'
})
con = urlopen(req).read().decode()

htmlObj = etree.HTML(con)

arr = htmlObj.xpath("//ul[@class='f-hide']/li/a/@href")
filenames = htmlObj.xpath("//ul[@class='f-hide']/li/a/text()")
ids = [ i[9:] for i in arr]
data = zip(filenames,ids)

def upload(filename,idnum):
    req = Request('https://music.163.com/song/media/outer/url?id=%s'%idnum,headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'referer':'https://music.163.com/'
    })

    res = urlopen(req).read()
    with open("songs/%s.mp3"%filename,"wb") as f:
        f.write(res)
    print("songs：《%s》 upload successed"%filename)



# for filename,idnum in data:
#     upload(filename,idnum)
upload(filenames[0],ids[0])