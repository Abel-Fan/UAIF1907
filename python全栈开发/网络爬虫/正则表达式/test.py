import re

# obj = re.search(r"\d+","yangfan1123456")
# # 返回一个匹配对象
# print(obj.group())

# obj = re.fullmatch("\d+","345678")
# print(obj)
# obj = re.split("[.;]","abc.def;gsdf",2)
# print(obj)

# obj = re.finditer(r"a(\w+)c(\w+)","abcdef")
# print(obj)

# def repl(patter):
#     if patter.group()!="":
#         return "陕西"
#     else:
#         return ""
# res = re.sub("山西",repl,"山西省山西博物院",count=1)
# print(res)

pattern = re.compile(r"a(?P<name>\w+)f(?P<age>\w+)")

obj = pattern.search("abcdefghijklmn")
if obj:
    print(obj.groupdict())