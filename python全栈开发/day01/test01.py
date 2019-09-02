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
str1 = "山西优逸客科技有限公司"
# print(str1[2:5:1])
# start 开始的下标，默认 0
# end 结束前的下标  默认 length
# step 步进值  可有可无 默认1
# print(str1[::])
# print(str1[-5:-1])
# print(str1[-1:-5:-1])


