# import time,datetime

# 日期的三种表示类型
# 1、时间戳
# print(time.time())
# 2、时间元组
# res = time.localtime(time.time())  # 将时间戳转换为时间元组
# 3、格式化时间
# date = time.strftime("%Y-%m-%d (%H:%M:%S)",res)  # 将时间元组转化为格式化时间
# print(date)


# timetuple = time.localtime(time.time())
# print( time.mktime(timetuple))

# datetime 模块包含类 （date time datetime timedelate）
from datetime import datetime,date,timedelta
import time

# date
d = date(2019,9,26)
# 实例化日期对象
# print(str(d))
# print("当前日期",date.today())
# 获取当前日期对象
# print(date.fromtimestamp(time.time()))
# 从时间戳获取日期对象


# date对象方法
# tring = d.strftime("%Y-%m-%d")
# 格式化时间
# t = d.timetuple()
# 转化为时间元组
# d = d.replace(year=2018)
# 替换时间 修改时间

# d = date.today()
# t = timedelta(days=2)
# print(d-t)
