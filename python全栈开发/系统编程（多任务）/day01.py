# 线程是cpu运算最小的单元
from threading import Thread,active_count,current_thread,enumerate,main_thread,stack_size,Lock
import time,random

# print(active_count()) # 返回当前活动线程的数量
# print(current_thread())  # 返回当前的线程
# print(enumerate()) # 返回当前活动的线程
# print(main_thread())  # 返回当前主线程
# print(stack_size()) # 返回创建线程时使用的栈的大小，如果指定size参数，则用来指定后续创建的线程使用的栈大小，size必须是0（表示使用系统默认值）或大于32K的正整数

# def task(num):
#     time.sleep(3)
#     print(num)
# start = time.time()
#
# arr = []
# for i in range(5):
#     # task(i)
#     t = Thread(target=task,args=(i,))
#     t.start()
#     arr.append(t)
#
# for t in arr:
#     t.join()
#
# end = time.time()
# print("运行总时间：%s" % (end - start))

# class Mytest(Thread):
#     def __int__(self):
#         super().__init__(self)
#     def run(self):
#         time.sleep(3)
#         print(self.name)
#
# t1 = Mytest()
# t1.start()

"""
Thread对象常用方法：
start() 运行线程
join(time) 阻塞主进程 time 阻塞时间
name 线程的名字
ident 线程的标识
is_alive() 判断线程是否存活
daemon 是否为守护线程 （守护线程：主线程不会等守护线程运行结束）
"""

# def task():
#     time.sleep(2)
#     print("task")
#
# t1 = Thread(target=task)
# t1.daemon = True
# t1.start()

# class Mytast(Thread):
#     def __init__(self):
#         super(Mytast,self).__init__()
#     def run(self):
#         time.sleep(2)
#         print(self.name)
#
# t1 = Mytast()
# t1.daemon = True
# t1.start()



# Thread(group=None,target,args=())  构造函数
"""
group 默认为None 为扩展Thread保留
target  线程启动执行函数
args 是元组 是线程执行函数的参数
kwargs  是线程执行函数的参数
"""

# 访问公共资源
hg = []
# 生产者消费者模式

# 锁
l1 = Lock()
l2 = Lock()

class Xm(Thread):
    def __init__(self):
        super(Xm,self).__init__()
    def run(self):
        while True:
            l1.locked()
            time.sleep(1)
            hg.append(1)
            print("小明放了1个鱼丸,锅内共有%s个鱼丸"%(len(hg)))
            l1.release()

class Xh(Thread):
    def __init__(self):
        super(Xh,self).__init__()
    def run(self):
        while True:
            l1.acquire()
            time.sleep(1)
            hg.pop(0)
            print("小红吃了1个鱼丸,锅内共有%s个鱼丸"%(len(hg)))
            l1.release()



xm = Xm()
xm.start()
xh = Xh()
xh.start()

