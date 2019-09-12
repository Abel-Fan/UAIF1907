from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(r"C:\Users\yangd\AppData\Local\Google\Chrome\Application\chromedriver.exe")

driver.get("https://accounts.douban.com/passport/login")
# 等待
time.sleep(3)
btn = driver.find_element_by_class_name("account-tab-account")

# 生成事件处理器
action = ActionChains(driver)
# 定义事件
eve = action.click(btn)
# 执行事件
eve.perform()

# 获取 username password

username = driver.find_elements_by_name('username')[0]
password = driver.find_elements_by_name('password')[0]

# 输入用户名密码

username.send_keys("17603514842")
password.send_keys("yangfan.")

# 获取登录按钮

a = driver.find_element_by_link_text("登录豆瓣")
action.click(a).perform()
time.sleep(3)

urls = ["https://movie.douban.com/subject/26794435/comments?start=%s&limit=20&sort=new_score&status=P"%i for i in range(0,481,20)]
index = 0
for url in urls:
    index+=1
    driver.get(url)
    time.sleep(3)
    data = driver.page_source
    with open("templates/%s.html"%index,"w",encoding='utf-8') as f:
        f.write(data)

driver.close()


