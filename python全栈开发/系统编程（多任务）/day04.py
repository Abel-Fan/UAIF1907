

"""
Manager
"""
# from multiprocessing import Process,Manager
# import time

# def fun(l,d):
#     l.append(6)
#     d['sex'] = '男'

# def fun2(l,d):
#     l.append(7)
#     d['weight'] = 50

# if __name__ == "__main__":
#     manage = Manager() # 创建一个管理器对象
#     l = manage.list([1,2,3,4,5])   # 创建 数据代理
#     d = manage.dict({'name':'小白','age':'18'}) # 创建 数据代理 
#     # Array Value
#     p = Process(target=fun,args=(l,d))
#     p.start()
#     p.join()
#     print(l,d)
#     p = Process(target=fun2,args=(l,d))
#     p.start()
#     p.join()
#     print(l,d)


"""
BaseManger 实现不同计算器数据共享
"""
# from multiprocessing.managers import BaseManager
# from queue import Queue
# class QueueManager(BaseManager): pass
# queue = Queue()
# queue.put("恭喜你 第一名")
# queue.put("恭喜你 第二名")
# queue.put("恭喜你 第三名")

# QueueManager.register("get_queue",callable=lambda : queue)

# m = QueueManager(address=('192.168.1.165',5000),authkey=b"horns")
# # 创建服务器
# serve = m.get_server()
# serve.serve_forever()


"""
pool 进程池
"""
from multiprocessing.pool import Pool
import time
def fun(i):
    time.sleep(1)
    sum = 0
    for i in range(0,100000):
        sum+=i
    print(i)

def fun2(x):
    return x**2

if __name__ == "__main__":
    pool = Pool(1)  # 5个进程的进程池

    # apply
    start = time.time()
    
    for i in range(100):
        # pool.apply(fun)
        pool.apply(fun,args=(i,))
    
    # res = list(map(lambda x,y:y*x,[1,2,3,4,5],["a","b","c","d"]))
    # print(res)
    # res =pool.map(fun2,[1,2,3,4,5])
    # print(res)

    end = time.time()
    print("运行总时间%s"%(end-start))
    

