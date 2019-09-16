import requests,json
import time
from fake_useragent import UserAgent
ua = UserAgent()
import re

class IfengSpider:
    def __init__(self):
        self.urls = [
            'https://news.ifeng.com/shanklist/3-35199-/',  # 台湾
            'https://news.ifeng.com/warmstory/', # 暖新闻
            'https://news.ifeng.com/xuanzhan2020/' # 宣战2020
        ]
        self.data = {
            #'':{'con':"",'edit':'','date':"",'source':''}
        }
    def newSpiderList(self,num):
        """
        新时代新气象 列表页
        :param num:
        :return:
        """
        url = 'https://shankapi.ifeng.com/autumn/xijinping/index/getCustomNewsTfList/0/%s/getCustomData?callback=getCustomData&_=120'%num

        resp = requests.get(url,headers={
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'User-Agent':ua.random
        })
        res = json.loads(resp.text[14:-1])
        data = res['data']['newsstream']
        for obj in data:
           yield obj['url']

    def newSpiderCon(self):
        urls = self.newSpiderList(5)
        for url in urls:

            resp = requests.get(url,headers={
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'User-Agent':ua.random
            })
            data = re.findall("var allData = (.+?);",resp.text)
            data = json.loads(data[0])["docData"]
            title = data['title']
            source = data['source']
            date = data['newsTime']
            edit = data['editorName']
            con = data['contentData']
            self.save(title=title,date=date,source=source,con=con,edit=edit)
            print("《%s》下载完成..."%title)
            time.sleep(5)

    def save(self,title,con,edit,date,source):
        if title not in self.data:
            self.data[title]={'con':con,'edit':edit,'date':date,'source':source}



s = IfengSpider()
s.newSpiderCon()
print(s.data)
