from multiprocessing import Process,active_children,cpu_count,current_process,get_all_start_methods,get_context,get_start_method,Queue
from threading import Thread

# 常用函数
"""
print("返回主进程中所有的子进程",active_children())
print("返回cpu的核心数",cpu_count())
print("返回当前进程",current_process())
print("获得进程全部开启方法",get_all_start_methods())
print("返回默认的上下文",get_context())
print("返回默认的进程开启方法",get_start_method())
"""

# 进程开启方法
"""
spawn
fork()
forkserver()
"""

# 创建进程

# （1）构造函数
import time,random
arr = []
def fun(i):
    time.sleep(random.randint(1,3))
    arr.append(i)
    print(arr)



# （2）继承类方式

class MyProcess(Process):
    def __init__(self):
        super(MyProcess,self).__init__()
    def run(self):
        fun()



"""
进程对象方法：
start()
run()
join()
name()
is_alive()
daemon
pid
authkey
exitcode
terminate
kill
close
"""
if __name__ == "__main__":
    
    q = Queue(2) 
    # 接收正整数 用来代表 队列的长度，如果是 -1 0 代表无限长
    """
    q.put() 插入内容
    q.get() 获取内容

    q.full() 是否已满
    q.empty() 是否为空

    q.task_done() 表示前面排队的任务已经被完成。
    q.join() 阻塞
    """
    # q.put(1)
    # q.put(2)
    # print(q.get())
    # q.put(3) # 阻塞
    # print(q.get())
    # print(q.get())
    # print(q.get()) # 阻塞

    # q.put(1)
    # print("qsize:",q.qsize())  #1
    # print("full:",q.full())    #False
    # print("empty",q.empty())   # False
    # q.put(2)
    # print("qsize:",q.qsize())
    # print("full:",q.full())
    # print("empty",q.empty())


# Queue 中 task_done() join() 联系
# from queue import Queue
# q = Queue(5)
# def fun1():
#     while True:
#         time.sleep(3)
#         q.put(1)
#         print("队列添加成功")
#         # q.task_done()

# def fun2():
#     while True:
#         q.join()
#         data = q.get()
#         print("获取内容%s"%data)

# t1 =  Thread(target=fun1)
# t1.start()
# t2 = Thread(target=fun2)
# t2.start()


# multiprocessing.Queue  没有 task_done() join()

# 利用 queue 进程进行同行
# import time
# q = Queue(5)
# def fun1(q): 
#     while True:
#         time.sleep(3)
#         q.put(1)
#         print("添加鱼丸,锅内还有%s"%q.qsize())
# def fun2(q):
#     while True:
#         data = q.get()
#         print('吃鱼丸,锅内还有%s'%q.qsize())
# if __name__ =="__main__":
#     p1 = Process(target=fun1,args=(q,))
#     p1.start()
#     p2 = Process(target=fun2,args=(q,))
#     p2.start()

from multiprocessing import Pipe
# Pipe() 管道
conn1,conn2 = Pipe(True) # 双工

def fun1(con):
    con.send("fun1：hello")
    print(con.recv())
def fun2(con):
    print(con.recv())
    con.send("fun2: hi")

if __name__ =="__main__":
    p1= Process(target=fun1,args=(conn1,))
    p1.start()
    p2 = Process(target=fun2,args=(conn2,))
    p2.start()