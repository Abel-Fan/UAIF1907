# 爬取电影影评


from urllib.request import urlopen
import lxml.etree as etree
import time,pickle

urls = ["https://movie.douban.com/subject/26794435/comments?start=%s&limit=20&sort=new_score&status=P"%i for i in range(0,201,20) ]


def getPage(url):
    con = urlopen(url).read().decode()
    htmlObj = etree.HTML(con)
    arr = htmlObj.xpath('//span[@class="short"]/text()')
    return arr

data = []
for url in urls:
    print("正在爬取%s"%url)
    data+=getPage(url)
    time.sleep(5)

res = getPage(urls[0])
print(res)

with open("哪吒之魔童降世 短评.txt","wb") as f:
    pickle.dump(data,f)
