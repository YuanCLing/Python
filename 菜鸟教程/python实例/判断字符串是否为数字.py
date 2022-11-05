def is_number(s):
    try:
        float(s)  # 如果能够转为浮点数
        return True
    except ValueError:  # 如果是标准异常“传入无效的参数”
        pass
    try:
        import unicodedata  # 处理ASCII码的包
        for i in s:
            unicodedata.numeric(i)  # 把一个表示数字的字符串转换为浮点数返回的函数
        return True
    except (TypeError, ValueError):
        pass
    return False

print(is_number('hdudu'))
print(is_number('1234'))

# str.isdigit() 检测字符串是否只由数字组成,只对正整数有效，负数、小数都不行
print('1234'.isdigit())

# isnumeric() 方法检测字符串是否只由数字组成，数字可以是： Unicode 数字，全角数字（双字节），罗马数字，汉字数字。
# 指数类似 ² 与分数类似 ½ 也属于数字
# str.isnumeric()
str = '²½1234'
print(f'{str} 全由数字组成：{str.isnumeric()}')
str = '\u0030'  # unicode for 0
print(f'{str} 全由数字组成：{str.isnumeric()}')

