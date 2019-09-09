# 迭代器 和 生成器
"""
for i in "abc":
    print(i)
for i in range(0,10):
    print(i)
for i in [1,2,3,4]:
    print(i)
"""
# 元组 、字典
# 为什么能够遍历呢？
# iter() 迭代器
# 作用：把要遍历的对象转换为迭代器对象
# 迭代器对象怎么被遍历 next()
# res = iter("abc")
# print(res)
# <str_iterator object at 0x0162DEB0>
# print( next(res) )
# print( next(res) )
# print( next(res) )
# print( next(res) )
# print( next(res) )
# for执行过程
# 1、将被遍历对象转化为迭代对象
# 2、通过next方式获取 迭代对象内容
# 3、捕获 stopiteraction 停止循环

# class Myiter:
#     def __init__(self,data):
#         # 要遍历的数据
#         self.data = data
#         self.index = len(data)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.index -= 1
#         if self.index>=0:
#             return self.data[self.index]
#         else:
#             raise StopIteration
#
# obj = Myiter("abcdefg")
# for i in obj:
#     print(i)

# 完成一个迭代器可正向可逆向

# class Myiter:
#     def __init__(self,data,type):
#         self.data = data
#         self.type = type   # 1 正向  -1 逆向
#         self.index = 0 if type==1 else len(self.data)-1
#     def __iter__(self): # for 隐式调用iter()
#         return self
#     def __next__(self):  # next()
#         if self.index>=len(self.data) or self.index<0 :
#             raise StopIteration
#         else:
#             res = self.data[self.index]
#             self.index+=self.type
#             return res
#
# for i in Myiter("abcdefg",1):
#     print(i)


# 生成器
# def mygen(data):
#     for i in range(0,data+1,1):
#         yield i

# return   :  终止函数   给函数一个返回值
#              可以设置多个return但只有一个能被运行

# yield    :  终止本次函数  给函数一个返回值
#
# for i in mygen(10):
#     print(i)

# print( (i*i for i in range(0,10)))

# class Mycontent:
#     def __enter__(self):
#         print("从上文进入程序")
#         return self
#     def __exit__(self,type,val,tb):
#         print("离开程序进入下文")
#         return True
#     def main(self):
#         print("hello world")
#         print(1/0)
#
# with Mycontent() as obj:
#     obj.main()


# import contextlib
# @contextlib.contextmanager
# def mycontext(filename):
#     #  上文
#     print('文件打开')
#     f = open(filename,"r")
#     # 过程
#     try:
#         yield f
#     except:
#         print("error")
#     # 下文
#     finally:
#         print("文件关闭")
#         f.close()
#
# with mycontext("demo.txt") as f:
#     res = f.read()
#     print(1/0)
#     print(res)


# class Mycontext:
#     def __init__(self,filename):
#         self.filename = filename
#     def __enter__(self):
#         print("文件打开")
#         self.f = open(self.filename,"r")
#         return self.f
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("文件关闭")
#         self.f.close()
#         print(exc_val)
#         return True
#
# with Mycontext("demo.txt") as f:
#     res = f.read()
#     print(1/0)
#     print(res)

# from contextlib import closing
# from urllib.request import urlopen
#
# with closing( urlopen('https://movie.douban.com/')) as f:
#     res = f.read().decode()
#     print(res)

# try:
#     # 可能有异常的代码
#     num = int(input("请输入一个数"))
#     print(num/0)
# except ValueError as v:
#     # 出现异常的处理方式
#     print(v)
# except ZeroDivisionError as z:
#     print(z)
# else:
#     # 没有错误执行else
#     pass
# finally:
#     # 一定会执行
#     pass


# class ShortInputExcept(Exception):
#     def __init__(self,min,num):
#         """
#         :param min: 最小输入
#         :param num: 本次输入
#         """
#         self.min = min
#         self.num = num
#
#     def __str__(self):
#         return '字符串长度不足%s,目前为%s'%(self.min,self.num)
#
# name = input("请输入你的名字")
# try:
#     if len(name)<2:
#         print(123)
#         raise ShortInputExcept(2,len(name))
# except ShortInputExcept as e:
#     print("长度不足")

#
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return "<Person %s %s>"%(self.name,self.age)
# p = Person("小明",19)
# print(p)