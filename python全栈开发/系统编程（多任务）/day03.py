# 线程： 是CPU调度的基本单位,包含在进程之中。
# 多线程 ，IO密集型程序
# 多进程 , 计算密集型程序

# 模块 threading
# 常用函数
from threading import Thread,active_count,current_thread,enumerate,main_thread,stack_size,Lock
"""
active_count() 获取当前活动线程数量
current_thread()  获取当前线程
enumerate()   获取当前活动线程
main_thread()  获取主线程
stack_size() 线程使用栈的大小
"""
# Thread
# 创建线程方式
#（1） 通过构造函数
"""
t = Thread(target=fun)  
# 参数
 target 线程执行功能 
 args fun的参数 
 kwargs fun的参数
 groups 线程扩展时使用 一般默认为None
 
# t 线程对象属性
t.start() 运行
t.join(blocking,timeout)  阻塞
t.name()  线程名字
t.ident() 线程id
t.daemon  是否为守护进程  默认 False 。 守护进程： 主进程不会等待守护进程运行结束。
t.is_alive() 判断线程是否存活
"""
# 通过继承类的方式
"""
class MyThread(Thread):
    def __init__(self):
        super(MyThread,self).__init__()
    def run(self):
        # 线程被 start()时执行的功能
        pass
        
t = MyThread()
t的属性同上
"""
# 线程的同步
# Lock 锁 原始锁 互斥锁
"""
l = Lock() 创建锁
l.acquire() 上锁
l.release() 释放锁
"""

# 死锁：两个都在阻塞等待对方释放的锁。

# RLock 递归锁,重复锁
# RLock 与 Lock 区别
# 1. 同一个线程内 RLock可以重复上锁 Lock释放锁才能上锁。
# 2. Lock 锁上的状态时可以释放锁, 释放状态的锁 释放时会报错
# 3. RLock是一个局部锁，在一个线程中上锁后，其他线程无法释放。Lock 全局锁

"""
r = RLock()
r.acquire()
r.release()
"""

# 条件锁 Condition
"""
c = Condition()
wait() 等待  阻塞当前线程 释放锁
notify() 通知  唤醒一个等待的线程
"""

# 信号量锁 Semaphore(num)
"""
信号量通常用于保护数量有限的资源，例如数据库服务器。在资源数量固定的任何情况下，都应该使用有界信号量。在生成任何工作线程前，应该在主线程中初始化信号量。
"""
"""
# 属性
s = Semaphore(5)
s.acquire()
s.release()
"""
# 事件锁Event,在内部维护一个状态
"""
e = Event()
e.is_set() 是否上锁
e.set()  上锁
e.clear()  释放锁
e.wait()  阻塞直到内部维护状态 为True
"""
# Timer 倒计时线程
"""
t = Timer(5,fun)  # 第一个参数倒计时时间  第二参数执行函数
t.start()
"""

# Barrier 栅栏锁