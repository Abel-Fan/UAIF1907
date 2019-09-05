# 推导式
# 分类：列表推导式  字典推导式 集合推导式
arr = [1,2,3,4,5,6]
arr1 = []
# for item in arr:
#     if item%2!=0:
#         arr1.append(item**2)

# arr1 = [ item**2 for item in arr if item%2!=0]
# print(arr1)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j}*{i}=%2d '%(i*j),end="")
#     print("")

# print("\n".join([  "".join([ f'{j}*{i}=%2d '%(i*j) for j in range(1,i+1)])  for i in range(1,10)]))



# 字典遍历
# for k in d1:
#     print(k)
#     print(d1.get(k,None))

# for k,v in d1.items():
#     print(k,v)

# d1.values()
# d1.keys()

# arr1 = [1,2,3,4,5]
# arr2 = ['a','b','c','d','e']

# for i,item in enumerate(arr2):
#     print(i,item)

# res = list(zip(arr1,arr2))
# print(res)

# 字典推导式
# d1 = {'a':[1,2,3],'b':[4,5,6],'c':[7,8,9]}
#
# d2 = { k+"1":v+['a'] for k,v in d1.items() if k in ['a','b']}
# print(d2)

# d1 = {'a':[1,2,3],'b':[4,5,6],'c':[7,8,9],'A':['a','b','c'],"B":['a']}
#
# d2 = { k.lower():d1.get(k.lower(),[])+d1.get(k.upper(),[])  for k,v in d1.items()}
# print(d2)
