from pyquery import PyQuery

# 初始化方式
# PyQuery(url="https://www.baidu.com")
# PyQuery("<html><div></div></html>")
# PyQuery(filename="index.html")

jquery = PyQuery(filename="index.html")
# box = jquery(".box")
# print(box.attr("class"))