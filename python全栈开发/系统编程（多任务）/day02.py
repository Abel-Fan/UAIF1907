from threading import Thread,Lock
import random
#  锁的作用
# arr = []
#
# #原始锁处于 "锁定" 或者 "非锁定" 两种状态之一。它被创建时为非锁定状态。它有两个基本方法， acquire() 和 release() 。当状态为非锁定时， acquire() 将状态改为 锁定 并立即返回。当状态是锁定时， acquire() 将阻塞至其他线程调用 release() 将其改为非锁定状态，然后 acquire() 调用重置其为锁定状态并返回。 release() 只在锁定状态下调用； 它将状态改为非锁定并立即返回。如果尝试释放一个非锁定的锁，则会引发 RuntimeError  异常。
#
# l = Lock()   # 状态默认是非锁定的
# l.acquire()
#
# def test1():
#     l.acquire()  # 如果之前的锁是锁定的，再次上锁发生阻塞
#                  # 如果之前的锁是非锁定的，可以实现上锁
#     arr.append(random.randint(1,10))
#
# t = Thread(target=test1)
# t.start()
#
#
#
# def test2():
#     arr.append(random.randint(1,0))



"""
爬取豆瓣电影top250
"""
# import requests
# import lxml.etree as etree
# urls = ["https://movie.douban.com/top250?start=%s"%i for i in range(0,226,25)]
#
# class Mytest(Thread):
#     def __init__(self):
#         super(Mytest,self).__init__()
#     def run(self):
#         while len(urls)>0:
#             url = urls.pop()
#             res = requests.get(url).text
#             html = etree.HTML(res)
#             titles = html.xpath("//div[@class='hd']/a/span[1]/text()")
#             print(self.name,titles)
#
# for i in range(2):
#     mytest = Mytest()
#     mytest.start()

"""
向列表中插入元素并打印列表
"""
# import time
# arr = []
# l = Lock()
# class Mytest(Thread):
#     def __init__(self):
#         super(Mytest,self).__init__()
#     def run(self):
#         time.sleep(1)
#         l.acquire()
#         arr.append(random.randint(0,10))
#         print(arr)
#         l.release()
#
# for i in range(20):
#     t = Mytest()
#     t.start()

"""
递归锁 复用锁 RLock()
在一个线程内可以重复上锁不被阻塞。
"""
# from threading import RLock
# import time
# r = RLock()
# l = Lock()
# def test1():
#     r.acquire()
#     r.acquire()
#     print("123")
#     time.sleep(2)
#     r.release()
#     r.release()
#
# def test2():
#     r.acquire()
#     print('test2')
#
# t = Thread(target=test1)
# t.start()
#
# t2 = Thread(target=test2)
# t2.start()


# 死锁
# import time
# l1 = Lock()
# l2 = Lock()
# def fun1():
#     l1.acquire()
#     print("fun1 is running")
#     time.sleep(1)
#     l2.acquire()   # 阻塞
#     print("fun1 is end")
#     l1.release()
#     l2.acquire()
# def fun2():
#     l2.acquire()
#     print("fun2 is running")
#     l1.acquire() # 阻塞
#     print("fun2 is end")
#     l2.release()
#     l1.release()
#
# t1 = Thread(target=fun1)
# t1.start()
# t2 = Thread(target=fun2)
# t2.start()

"""
锁的上下文使用方法

向列表中插入元素并打印列表
"""
# import time,random
# arr = []
# l = Lock()
# def fun():
#     time.sleep(1)
#     with l:  # 上锁   自动解锁的功能
#         arr.append(random.randint(0,10))
#         print(arr)
#
# for i in range(20):
#     t = Thread(target=fun)
#     t.start()

"""
条件锁
class Condition(lock=RLock)  默认是递归锁

方法：
acquire()  上锁
release() 释放锁

wait(timeout=) 等待(释放锁) 阻塞(等待被通知)
notify(n=) 通知 唤醒n个线程


wait_for(predicate,timeout=)  predicate 是一个函数 返回 True False
notify_all() 唤醒所有线程
"""
# from threading import Condition
# import time
# con = Condition(lock=Lock())
#
# arr = []
#
# class XM(Thread):
#     def __init__(self):
#         super(XM,self).__init__()
#     def run(self):
#         with con:
#             while True:
#                 time.sleep(1)
#                 arr.append(1)
#                 length = len(arr)
#                 print("小明添加了1个鱼丸,锅内还有%s个鱼丸"%length)
#                 if length>=5:
#                     con.notify_all()
#                     con.wait()
#
#
# class XH(Thread):
#     def __init__(self,name):
#         super(XH,self).__init__()
#         self.name = name
#     def run(self):
#         with con:
#             while True:
#                 time.sleep(1)
#                 arr.pop()
#                 length = len(arr)
#                 print("%s吃了1个鱼丸,锅内还有%s个鱼丸"%(self.name,length))
#                 if length<=0:
#                     con.notify()
#                     con.wait()
#
# xm = XM()
# xm.start()
#
# xh = XH("小红1")
# xh.start()
#
# xh1 = XH("小红2")
# xh1.start()


"""
wait_for(predicate,timeout=)
等待 当predicate 返回值为 False 阻塞  当返回值为True 运行
wait() 等待，阻塞 。直到被 notify
"""
# from threading import Condition
# import time
# con = Condition()
# con.acquire()
#
# def fun():
#     time.sleep(5)
#     return True
# con.wait_for(fun)
# print(123)

"""
Semaphore 信号量对象

信号量通常用于保护数量有限的资源，例如数据库服务器。在资源数量固定的任何情况下，都应该使用有界信号量。在生成任何工作线程前，应该在主线程中初始化信号量。
"""
# from threading import Semaphore
# import time
# b = Semaphore(value=3)

# 技术面试 每次3个人

# class Ms(Thread):
#     def __init__(self):
#         super(Ms,self).__init__()
#     def run(self):
#         with b:
#             print("<%s>开始面试，倒计时3秒钟"%self.name)
#             time.sleep(3)
#             print("<%s>面试结束，有请下一个同学"%self.name)
#
#
# for i in range(20):
#     m = Ms()
#     m.start()


"""
事件锁
is_set() 判断事件锁内部开关是否为true 
set() 设置事件锁内部开关为 true
clear() 设置事件锁内部开关为 false
wait()  阻塞 等待事件锁内部开关为true 然后运行

"""
# from threading import Event
# import time
#
# e1 = Event()
# e1.set()
#
# e2 = Event()
#
# arr = []
# class XM(Thread):
#     def __init__(self):
#         super(XM,self).__init__()
#     def run(self):
#         while True:
#             e1.wait()
#             time.sleep(1)
#             arr.append(1)
#             length = len(arr)
#             print("小明添加了1个鱼丸，锅内还有%s个鱼丸"%length)
#             if length>=5:
#                 e1.clear()
#                 e2.set()
#
# class XH(Thread):
#     def __init__(self):
#         super(XH, self).__init__()
#     def run(self):
#         while True:
#             e2.wait()
#             time.sleep(1)
#             arr.pop()
#             length = len(arr)
#             print("小红吃了1个鱼丸,锅内还剩%s个鱼丸"%length)
#             if length<=0:
#                 e2.clear()
#                 e1.set()
#
# xm = XM()
# xm.start()
# xh = XH()
# xh.start()

"""
定时器对象
"""
# import time
# def fun():
#     time.sleep(3)
#     print("123")
#
# fun()
# print("开始")

# from threading import Timer
# # Timer 是一个倒计时线程
# def fun():
#     print("123")
#
# t = Timer(3,fun)
# t.start()
# print("开始")


"""
栅栏对象

wait()

"""
# from threading import Barrier,active_count
# import time
#
# b = Barrier(5)
# l = Lock()
#
# class Test(Thread):
#     def __init__(self):
#         super(Test,self).__init__()
#     def run(self):
#         b.wait()
#         with l:
#             print("%s 开始运行"%self.name)
#
# for i in range(20):
#     time.sleep(2)
#     t = Test()
#     with l:
#         print("创建了%s线程"%t.name)
#     t.start()