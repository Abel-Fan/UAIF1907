from pyquery import PyQuery
from fake_useragent import UserAgent
import pickle

ua = UserAgent()

url = "https://www.amz520.com/amztools/amusestimator.html"
dom = PyQuery(url,headers={
    'User-Agent':ua.random
})

essiteselect = dom("#essiteselect option").text()
ids = [  dom(ele).attr("value") for ele in dom("#essiteselect option")]

arr = essiteselect.split()


def getOptions(countryId):
    obj = {}
    for options in dom("#selectcate%s option"%countryId):
        text = dom(options).text()
        value = dom(options).attr("value")
        obj[text]=value
    return obj


obj = {}
for i in range(0,len(arr)):
   
    data = {}
    data['id'] = ids[i]
    data['options'] = getOptions(ids[i])
    obj[arr[i]]=data



# {"美国":{id:1,options:{'':1}}}

with open("country.txt","wb") as f:
    pickle.dump(obj,f)

