# 函数
# 语法
"""
函数的定义：
def 函数名([形参]...):
    函数体
    [return 返回值]

函数的调用:
函数名([实参])

"""
# def fn(a,b):
#     return a+b
# res = fn(10,20)
# print(res)

# 参数的用法
"""
1. 必选参数
2. 缺省参数，默认参数。
    注意：默认参数只创建一次，默认参数必须放在必选参数之后
def fn(a,b=10):
    return a+b
fn(20)

def fn(a,b=[]):
    b.append(a)
    
# def fn(a,b=[]):
#     b.append(a)
#     print(b)

# fn(10)  # [10]
# fn(20)  # [10,20]
# fn(30)  # [10,20,30]
# fn(10,[])  # [10]
# fn(20,[])  # [20]
# fn(30,[])  # [30]

3、可变参数

def fn(*args):
    pass
    
def mysum(a,b,*args):
    print(a,b,args)
mysum(1,2,3,4,5,6,7,8,9)

4. 关键字参数
def getUserInfo(**kwargs):
    print(kwargs)

getUserInfo(age=19,sex=12)

参数顺序：
必选参数 > 缺省参数 > 可变参数 > 关键字参数

解包

def fn(a,b,c):
    print(a,b,c)
"""
# def fn(a,b,c):
#     print(a,b,c)
#
# t = [10,20,30]
# fn(*t)

# def fn(name,age):
#     print(name,age)

# fn("xb",19)
# d1 = {'name':'xb','age':10}
# fn(**d1)

# 返回值用法

# def fn():
#     return 1,2,3,4,5
# res = fn()
# a,b,c,d,e = fn()
# print(res,a,b,c,d,e)

# 名词解释
# 闭包
# 两个发生嵌套关系的函数，内部函数使用外部函数的变量，在全局情况下使用内部函数时发生闭包。保护数据
# def fn():
#     arr = []
#     def newFn(a):
#         arr.append(a)
#         print(arr)
#     return newFn

# newFn = fn()
# newFn(1)
# newFn(2)
# newFn(3)
# newFn(4)


# 高阶函数  柯里化
# mysum(1)(2)(3)

# def mysum(a):
#     def mysum2(b):
#         def mysum3(c):
#             return a+b+c
#         return mysum3
#     return mysum2
#
# res = mysum(10)(20)(30)
# print(res)

# 递归:
# def jc(num):
#     if num==1:
#         return 1
#     else:
#         return num*jc(num-1)

# def jc(num):
#     return   1   if num==1 else  num*jc(num-1)

# 装饰器
# 功能： 给原函数添加新的功能
# 特点，原则：1.不改变原函数   2.不改变原函数的调用方式  3.同时满足 1 and 2
import time

def fn():
    time.sleep(1)
    print("hello world")

def fn1():
    time.sleep(1)
    print("hello")

def fn2(fn):
    def newFn():
        start = time.time()
        fn()
        end = time.time()
        print(f"总时间为：{end-start}")
    return newFn

# fn2(fn1)()
# fn2(fn)()
fn = fn2(fn)
fn1 = fn2(fn1)

fn()
fn1()