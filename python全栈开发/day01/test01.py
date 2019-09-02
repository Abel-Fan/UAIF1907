# 单行注释
"""
多行注释
"""
'''
注释
'''

# 语法特点：
# 严格遵循缩进原则,不要轻易使用空格
"""
    print("123")
    ^
IndentationError: unexpected indent
"""

# 输入工具
# input("提示信息")
# input("请输入一个数:")

# 输出工具 print()
# print([变量|数据|表达式]*)
"""
print(123)
print(123+123)
print(name,123,123+123)
"""

# 变量
"""
1、一般赋值
name = '小明'
2、多元赋值
a,b,c = 1,2,3
3、链式赋值
a=b=c=1
"""
# a,b,c=1,2,3
# print(a,b,c)
# a=b=c="a"
# print(a,b,c)

# 变量的命名规则：
"""
1. 变量名由 字母数字下划线构成，数字不能开头，支持汉字
2. 严格区分大小写
3. 语义化
4. 不能使用关键字和保留字
"""

# 数据类型
# 1、数字类型
# 整数int 浮点数float
# 0b二进制  0o八进制 0x开头
# 3e2

# 2、字符串类型 str
# 字符编码： ASCII GBK GB2312 UTF-8 unicode
# 字符串定义： ''  ""   """ """   '''  '''
# 转义字符：\'  \" \\  \t \r \n
# 前缀
#  r"abc"  取消转义
#  u"abc"
#  b"abc"
#  f"abc"  模板字符串
# name='小白'
# print(f"{name} 你好")

# 模板字符串
# name = "小白"
# print(f"{name}你好")
# print("%s你好"%name)  # %s str
# print("我有%d个手机"%10)           # %d 整型
# print("day%2d"%10)
# print("day%2d"%1)
# print("价格为%0.2f元"%10)
# print("%s你好，这里有%d个手机，一共价值%0.2f元"%("小白",10,10000))
# 字符串访问
# str1[index]  index可以为 负
# print(str1[-1])
# 切片
# 语法 "abcdef"[start:end:step]
# str1 = "山西优逸客科技有限公司"
# print(str1[2:5:1])
# start 开始的下标，默认 0
# end 结束前的下标  默认 length
# step 步进值  可有可无 默认1
# print(str1[::])
# print(str1[-5:-1])
# print(str1[-1:-5:-1])

# None
# bool True False

# 列表：
# arr = []
# 注意：
"""
1、可以定义空列表
2、可以定义只有一个元素的列表
3、元素可以是任意类型
"""
# 列表的操作
# 增加
# arr = []
# arr.append() # 末位添加
# arr.append("abc")
# arr.insert(0,"123")
# print(arr)
# 访问
# arr[index]
# 修改
# arr[index]
# 删除
arr = [1,2,3,4]
# arr.remove(1)
# arr.pop(0)
# arr.clear()
# del arr[0]
# print(arr)
# print(dir(arr))

# str1 = "山西硬汉科技有限公司"
# str2 = "山西优逸客科技有限公司"
# str3 = "陕西优逸客科技有限公司"
# print(str2[:-4])

# 元组
# t1 = ()
# 注意
"""
1、可以定义没有元素的元组
2、也可以定义只有一个元素的元组 (1,)
3、元组是不可改变的列表
"""
# arr1 = [1,2,3]
#
# t1 = (1,2,3)
# t1[0] = 'a'

# t1 = ([1,2],[3,4])
# t1[0][0] = 'a'
# print(t1)

# 字典 dict
# d1 = {'name':'xb','age':19}
# name = 'name1'
# d1 = {(1,2,4):'xb','age':19}
# print(d1)
# 注意
# 1. 字典的键值是没有顺序的
# 2. 字典的键是不可变量（  数字类型 字符串 None True False   ）

# 字典的基本操作
# 增
# d1 = {'name':'xb','age':19}
# d1['sex'] = '男'
# print(d1)
#
# d1.update({'sex':'男'})
# print(d1)

# 删除
# d1.pop("name")
# d1.popitem()  # 末位删除
# del d1['name']
# d1.clear()
# print(d1)

# 修改
# d1['name'] = ""

# 访问
# print(d1['name'])
# print(d1.get('sex','暂无'))

# 集合 set
# s = {1,2,3,4,5,6}
# 注意：集合是不重复的

# 集合基本操作
# 增加
# s = {1,2,3,4,5,6}
# s.update({7,8,9})
# s.update("abcdef")
# s.update(['aa','bb'])
# s.add()
# print(s)


# 删除
# s = {1,2,3,4,5,6}
# s1 = {5,6,7,8,9}
# s.pop()   # 首位删除
# s.remove(2)
# s.clear()
# print(s)

# 交集
# print(s&s1)
# 并集
# print(s|s1)
# 补集
# print(s^s1)

# int float bool None list tuple dict set
# 可变数据类型：list dict set

# 测试数据类型
# type()

# 运算符
# 算术运算符
# + - * / %
# // **
# + 可以连接 字符串 列表元组
# * 重复 字符串 列表 元组

# print("abc"+"bcd")
# print([1,2,3]+[4,5,6])
# print((1,2,3)+(4,5,6))
# print("abc"*3)
# print([1,2,3]*3)
# print((1,2,3)*3)


# / 结果为float
# print(10/2)

# //
# print(10//3)  # 向下取整

# ** 幂运算
# print(2**10)

# 赋值运算符
# = += -= *= /= %= //= **=

# 关系运算符
# > >= < <= == !=
# not in  in  包含    is not  is  是否为同一个
# print(1 not in [1,2,3] )

# name = 'xb'
# name2 = 'xb'
# name2 = "xh"
# print(name is name2)

#  逻辑运算符
# and or not
# 严格遵循短路原则

# 三元运算符
# print("1>2") if 1>2 else print("2>1")

# 一元运算符
# del

# 运算符的优先级


# 流程控制

# 分支语句

# if 条件:
#     代码块
# elif 条件2:
#     代码块
# else:
#     代码块

# 循环语句
# for
# while
# while 条件:
#     pass
#
# arr = [1,2,3,4,5,6]
#
# for item in arr:
#     print(item)

# arr = range(1,100,1)   # 生成生成器
# print(list(arr))

# for i in range(0,10):
#     print(i)

# break continue

# for i in range(0,10):
#     print(i)
#     if i==5:
#         break
# else:
#     print("结束")


# 数据类型转换
# int()
# float()
# str()
# bool()
# dict()
# set()
# tuple()