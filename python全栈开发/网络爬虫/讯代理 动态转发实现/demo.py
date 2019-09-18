import sys
import time
import hashlib
import requests
import urllib3
from lxml import etree

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
_version = sys.version_info

is_python3 = (_version[0] == 3)

orderno = "ZF20199183769jXKFig"
secret = "d7698936938a4bd583be7cf854135a8a"

ip = "forward.xdaili.cn"
port = "80"

ip_port = ip + ":" + port

timestamp = str(int(time.time()))              
string = ""
string = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp

if is_python3:                          
    string = string.encode()

md5_string = hashlib.md5(string).hexdigest()                
sign = md5_string.upper()                             
#print(sign)
auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp

#print(auth)
proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
headers = {"Proxy-Authorization": auth, "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}



r = requests.get("https://movie.douban.com/top250", headers=headers, proxies=proxy, verify=False,allow_redirects=False)

print(r.request.headers)