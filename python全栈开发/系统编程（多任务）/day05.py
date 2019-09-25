# 协程

"""
yield 实现协程方式
"""
# yield
# import time

# arr = []
# def XM(gen):
#     while True:
#         if len(arr)<=0:
#             for i in range(5):
#                 time.sleep(1)
#                 arr.append(1)
#                 print("小明添加了一个鱼丸,锅内还有%s个"%len(arr))
#         elif len(arr)>=5:
#             # 调用消费者
#             for i in range(5):
#                 next(gen)

# def XH():
#     while True:
#         time.sleep(1)
#         arr.pop()
#         print("小红吃了一个鱼丸,锅内含有%s"%len(arr))
#         yield
        
# gen = XH()
# XM(gen)

"""
额外补充
生成器中 send()  next()
"""

# def fun():
#     for i in range(10):
#         data=yield i
#         print("data",data)

# gen = fun()  # 创建生成器
# print(next(gen))   # gen.__next__()
# # print(next(gen))  next 传入到 yield i 默认 为 None
# print(gen.send(10)) #  next() =>  gen.send(None)

"""
greenlet 实现协程

"""
# from greenlet import greenlet
# import time
# arr = []
# def xm():
#     while True:
#         for i in range(5):
#             time.sleep(1)
#             arr.append(1)
#             print("小明添加了一个鱼丸，锅内还有%s个鱼丸"%len(arr))
#         # 调用消费者
#         f2.switch()

# def xh():
#     while True:
#         for i in range(5):
#             time.sleep(1)
#             arr.pop()
#             print("小红吃了一个鱼丸，锅内还有%s个鱼丸"%len(arr))
#         # 调用生产者
#         f1.switch()

# f1 = greenlet(xm)
# f2 = greenlet(xh)
# f1.switch()


"""
gevent 方式实现协程

"""
# import gevent

# def fun1():
#     print("白日依山尽")
#     gevent.sleep(2)
#     print("欲穷千里目")
   
# def fun2():
#     gevent.sleep(1)
#     print('黄河入海流')
#     gevent.sleep(3)
#     print("更上一层楼")

# f1 = gevent.spawn(fun1)
# f2 = gevent.spawn(fun2)
# gevent.joinall([f1,f2])


# 利用gevent中monkey补丁实现 协程并发
# import gevent
# from gevent import monkey
# import requests
# import lxml.etree as etree

# monkey.patch_all()

# urls = ['https://movie.douban.com/top250?start=%s'%i for i in range(0,226,25)]

# def getCon(url):
#     con = requests.get(url)
#     htmlObj = etree.HTML(con.text)
#     title = htmlObj.xpath("//span[@class='title'][1]/text()")
#     print(title)

# spawns = [   gevent.spawn(getCon,url=url)   for url in urls]

# gevent.joinall(spawns)


"""
async 实现协程
"""
# import asyncio,time

# async def main():
#     print("hello")
#     await asyncio.sleep(1)
#     print("world")

# asyncio.run(main())
# arr = []
# async def xm():
#     while True:
#         time.sleep(1)
#         arr.append(1)
#         print("小明添加了一个鱼丸,锅内还有%s"%len(arr))
#         if len(arr)>=5:
#             break

# async def xh():
#     while True:
#         await xm()
#         for i in range(len(arr)):
#             arr.pop()
#             print("小红吃了一个鱼丸,锅内还有%s"%len(arr))


# async def main():
#     asyncio.create_task(xh())

# asyncio.run(main())
