# 线程是cpu运算最小的单元
from threading import Thread,active_count,current_thread,enumerate,main_thread,stack_size
import time,random

# print(active_count()) # 返回当前活动线程的数量
# print(current_thread())  # 返回当前的线程
# print(enumerate()) # 返回当前活动的线程
# print(main_thread())  # 返回当前主线程
# print(stack_size()) # 返回创建线程时使用的栈的大小，如果指定size参数，则用来指定后续创建的线程使用的栈大小，size必须是0（表示使用系统默认值）或大于32K的正整数

def task(num):
    time.sleep(3)
    print(num)
start = time.time()

arr = []
for i in range(5):
    # task(i)
    t = Thread(target=task,args=(i,))
    t.start()
    arr.append(t)


for t in arr:
    t.join()

end = time.time()
print("运行总时间：%s" % (end - start))