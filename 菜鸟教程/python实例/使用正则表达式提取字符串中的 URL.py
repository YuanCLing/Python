# URL 统一资源定位器
# 正则表达式：一种文本模式，包括普通字符和特殊字符。描述了一种字符串匹配的模式。
"""
runoo+b，可以匹配 runoob、runooob、runoooooob 等，+ 号代表前面的字符必须至少出现一次（1次或多次）。

runoo*b，可以匹配 runob、runoob、runoooooob 等，* 号代表前面的字符可以不出现，也可以出现一次或者多次（0次、或1次、或多次）。

colou?r 可以匹配 color 或者 colour，? 问号代表前面的字符最多只可以出现一次（0次或1次）
"""

import re


def Find(string):
    # findall() 查找所有匹配正则表达式的字符串
    url = re.findall('https?://(?:[-\w.]|(?:%[0-9a-fA-F]{2}))+', string)
    return url


string = 'Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：https://www.google.com'
print("Urls: ", Find(string))

# […]   字符集，匹配多项
# [\w.-]    匹配字母、数字、下划线  .号以及-号
# \w    匹配字母、数字、下划线
# \d    匹配一个数字字符，等价于 [0-9]
# .     匹配除换行符之外的任何单字符
# {n}   匹配确定的次数
# {n,}  至少匹配的次数
# {n,m} 至少匹配n次数,至多匹配m次
