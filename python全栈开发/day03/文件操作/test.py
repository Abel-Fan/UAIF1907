# open('fileurl','mode',error,encodeing)

# mode
"""
r  读
w  写入(重写),文件不存在则创建并写入,文件指针始终在文件头
a  追加,文件不存在则创建并写入,文件指针始终在文件尾
rb、wb、ab是在 r、w、a模式基础上以二进制方式操作文件
r+ 读写,不创建新文件,每次操作从文件头开始
w+ 读写,创建新文件,每次操作从文件头开始
a+ 读写,创建新文件,每次操作从文件尾开始
rb+、wb+、ab+ 在r+\w+\a+模式基础上以二进制方式操作文件
"""
# error 错误处理
# strict 出现错误报错
# ignore 出现错误忽略

# encoding 字符编码
# utf-8 gbk


# 文件对象内建函数
# 读
## 1. fobj.read([num]) num 指定读取字符
## 2. fobj.readline([num]) 读取每行字符
#     指定读取多少行（\r\n 代表行结束|EOF代表文件结束）
## 3. fobj.readlines() 读取全部行

# 写
# fobj.write(data)   写入数据
# fobj.writelines()  写入多行

# fobj.write("山西优\r\n逸客")

# 文件操作步骤
# 1、打开
# 2、操作（读写）
# 3、关闭
# fobj = open('a.txt',"r+")
# # res = fobj.read()
# res1=fobj.readline(2)
# res2=fobj.readline(2)
# print(res1,res2)
# fobj.close()



# 指针偏移
# fobj.seek(p,0)  从文件头开始指针位数 绝对位置。
# fobj.seek(p,1)  从当前指针开始移动指针位数,只适用于以二进制形式打开的文件
# fobj.seek(p,2)  从文件尾开始指针位数。只适用于以二进制形式打开的文件

# 关闭文件
# fobj.close() 将缓存数据写入硬盘并且关闭文件
# fobj.flush() 将缓存数据写入硬盘

import csv

# with open('c.csv','r',newline='',encoding="utf-8") as f:
    # 写
    # writer = csv.writer(f,dialect='excel')
    # writer.writerow(['a','b','c'])
    # 读
    # reader = csv.reader(f,dialect="excel")
    # for data in reader:
    #     print(data)

    # writer = csv.DictWriter(f,['name','age'])
    # writer.writeheader()
    # writer.writerows([
    #     {'name':'小白','age':'18'},
    #     {'name':'夏红','age':23}
    # ])

    # reader = csv.DictReader(f)
    # for data in reader:
    #     print(data)

# def csv_write(path,data):
#     with open(path,'w',encoding='utf-8',newline='') as f:
#         writer = csv.writer(f,dialect='excel')
#         for row in data:
#             print(row)
#             writer.writerow(row)
#     return True
#
# data = [
#     ['Name','Height'],
#     ['Keys','176cm'],
#     ['HongPing','160cm'],
#     ['WenChao','176cm']
# ]
#
# csv_write('test.csv',data)