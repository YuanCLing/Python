# 实例1 使用 update() 方法，第二个参数合并第一个参数
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
print(dict2.update(dict1))  # update 返回None
print(dict2)  # dict2合并了dict1


# 实例2 使用 **，函数将参数以字典的形式导入
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = {**dict1, **dict2}
print(dict3)