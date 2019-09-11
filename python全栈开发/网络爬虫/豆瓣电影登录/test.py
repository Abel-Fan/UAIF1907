from urllib.request import urlopen,Request,HTTPHandler,ProxyHandler,build_opener,HTTPCookieProcessor
import http.cookiejar

from urllib.parse import parse_qs
import json

url='https://accounts.douban.com/j/mobile/login/basic'
data = {
    'name':'17603514842',
    'password':'yangfan.',
    'remember':'false'
}

req = Request(url,headers={
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
},data=b'ck=&name=17603514842&password=yangfan.&remember=false&ticket=')

# 最简单的构造器
# httphandler = HTTPHandler(debuglevel=1)  # 构造处理器
# open = build_opener(httphandler)  # 构造 opener
# con = open.open(req).read()

# 代理管理器
# proxyhandly = ProxyHandler({
#     'http':'http://58.253.144.230:61234',
#     'https':'https://163.204.241.239:9999'
# })
# opener = build_opener(proxyhandly)

# rep = opener.open(req).read()
# print(rep)


# 创建cookiejar对象
cookie = http.cookiejar.CookieJar()
# 构造handler管理器
handler = HTTPCookieProcessor(cookie)
opener = build_opener(handler)
con = opener.open(req).read()


req2=Request("https://movie.douban.com/subject/26794435/comments?start=300&amp;limit=20&amp;sort=new_score&amp;status=P",
             headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
})

res = opener.open(req2)
print(res.read().decode())