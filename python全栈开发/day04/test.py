# open()
# 操作 r  w
# close()

# 捕获异常

# try:
#     f = open("a.txt",'r',encoding="utf-8")
#     data = f.readlines()
#     print(10/0)
#     print(data)
# finally:
#     print("文件关闭")
#     f.close()
# 上下文管理器
# with open("a.txt",'r') as f:
#     data = f.readlines()
#     print(data)

# csv文件操作
import csv
# with open('a.csv','r+',newline="",encoding="utf-8") as f:
    # 写
    # writer = csv.writer(f)
    # for _ in range(0,10):
    #     writer.writerow(['a','b','c'])

    # writer.writerows([
    #     ["a",'b','c'],
    #     ["d",'e','f']
    # ])

    # 读
    # reader = csv.reader(f)
    # for row in reader:
    #     print(row)

    # dict方式
    # writer = csv.DictWriter(f,['id','name','age'])
    # writer.writeheader()
    # # writer.writerow()
    # writer.writerows([
    #     {'id':1,'name':'小白','age':18},
    #     {'id': 2, 'name': '小红', 'age': 18},
    #     {'id': 3, 'name': '小黑', 'age': 18},
    # ])
    # reader = csv.DictReader(f,['id','name','age'])
    # for row in reader:
    #     print(dict(row))

# 持久化存储
#
import pickle
# arr = ['name',19,123,True]

# 写入
# with open("data.txt","rb") as f:
    # pickle.dump(arr,f)
    # arr = pickle.load(f)
    # print(arr)
    # print(arr[0])