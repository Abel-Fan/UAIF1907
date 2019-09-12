import requests
# url = "https://www.toutiao.com/stream/widget/local_weather/city/"
# res = requests.get(url)
# print(type(res.json()))



# url = "https://movie.douban.com/top250"
# params = {'start':0}
# rsp = requests.get(url,params=params,headers={
#
# })

# rsp = requests.post(url,data={})

# print(rsp.url)  # 获取请求地址
# print(rsp.text)  # 获取详情内容 utf-8
# print(rsp.content)  # 获取详情内容 字节
# rsp.json()

data = {
    'name':'17603514842',
    'password':'yangfan.',
    'remember':'false'
}
url = 'https://accounts.douban.com/j/mobile/login/basic'
res = requests.post(url,data=data,verify=False)
print(res.json())

requests.request("")
