import xlrd,xlwt
from pyquery import PyQuery
from fake_useragent import UserAgent
import requests,re,pickle

ua = UserAgent()
with open("country.txt","rb") as f:
    country = pickle.load(f) 


# 读取数据
book = xlrd.open_workbook("data.xlsx")
sheet = book.sheet_by_index(0)

def getUrls():
    for row in range(1,sheet.nrows):
        url = sheet.cell_value(row,1)
        status = sheet.cell_value(row,2)
        country = sheet.cell_value(row,3)
        yield url,status,country


# 爬取category  ranking
def getCateRank(url):
    dom = PyQuery(url,headers={
        'User-Agent':ua.random
    })
    category = " ".join(dom("#wayfinding-breadcrumbs_feature_div>ul>li:nth-child(1)>span>a").text().split())
    if dom("#SalesRank"):
        ranking = re.findall("#([\d,]+?)\s",dom("#SalesRank").text())[0].replace(",","")
    else:
        res = requests.get(url,headers={
            'User-Agent':ua.random
        })
        ranking = re.findall("#([\d,]+?)\s[\s\w]+?\(",res.text)[0].replace(",","")
    return category,ranking

# book = xlwt.Workbook("data.xlsx")
# sheet = book.add_sheet("Sheet1")

# 获取销量
def getSales(rank,categoryid,esselect):
    try:
        response = requests.post('https://www.amz520.com/tool/get_bsrranksales',headers={
            'User-Agent':ua.random
        },data={
            'rank':rank,
            'categoryid':categoryid,
            'esselect':esselect
        })
        res = response.json()
    except:
        return "数据异常"
    else:
        if res.get("ames",None)!=None:
            return res['ames']['estsalesresult']
        else:
            return "没有数据"

# {"美国":{id:1,options:{'':1}}}
def getCageIdCounId(cate,coun):
    counid = country.get(coun)['id']
    cateid = country[coun]['options'][cate]
    return cateid,counid


def save():
    index = 0
    for url,status,countryname in getUrls():
        index+=1
        try:
            categoryname,ranking = getCateRank(url)
            categoryID,countryID = getCageIdCounId(categoryname,countryname)
            sale = getSales(ranking,categoryID,countryID)
            print(index,ranking,categoryname,categoryID,countryname,countryID,sale)
        except BaseException as e:
            print(e)
        
            

        

if __name__ =="__main__":
    save()
    


