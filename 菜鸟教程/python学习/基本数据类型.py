# 多个变量赋值
a = b = c = 1
a, b, c = 1, 2, 3

# 标准数据类型
# 不可变： Number String Tuple
# 可变：   List  Dictionary Set
# type(a)
# isinstance(a, int) 会认为子类是一种父类类型
# 删除一些对象
# del var1，var2
"""
一个变量可以通过赋值指向不同类型的对象。
数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
在混合计算时，Python会把整型转换成为浮点数.
"""

# 字符串String ' ' 不可变
"""
Python 字符串不能被改变。向一个索引位置赋值，比如 word[0] = 'm' 会导致错误。
注意：
1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
2、字符串可以用+运算符连接在一起，用*运算符重复。
3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
4、Python中的字符串不能改变
"""
str = '12345'
print(str[-1::-1])  # 翻转字符串
print('----------------')
# 通过空格将字符串分隔符，把各个单词分隔为列表
# inputWords = input.split(" ")
# 重新组合字符串
# output = ' '.join(inputWords)

# 列表List [] 可变
"""
与Python字符串不一样的是，列表中的元素是可以改变的.
1、List写在方括号之间，元素用逗号隔开。
2、和字符串一样，list可以被索引和切片。
3、List可以使用+操作符进行拼接。
4、List中的元素是可以改变的
"""
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']
print(list)         # 输出完整列表
print(list[0])      # 输出列表第一个元素
print(list[1:3])    # 从第二个开始输出到第三个元素
print(list[2:])     # 输出从第三个元素开始的所有元素
print(tinylist * 2)     # 输出两次列表
print(list + tinylist)  # 连接列表
list[2:3] = []      # 将对应元素设置为[],删除了
print(list)
list[2:3] = [5]     # 必须依旧用列表修改
print(list)
print(list[-1::-1]) # 反转列表：第一个-1表示最后一个元素，第二个表示逆向


# 元组Tuple () 不可变
"""
1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
4、元组也可以使用+操作符进行拼接
"""
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号


# 集合Set {}
"""
创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
重复的元素被自动去掉
"""
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)   # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素
print('--------------------------')


# Dictionary字典 {}
"""
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
"""

