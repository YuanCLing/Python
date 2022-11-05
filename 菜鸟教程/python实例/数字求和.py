# 第一种
num1 = input("输入第一个数字：")
num2 = input("输入第二个数字：")
sum = float(num1) + float(num2)
print(f"数字{num1}和{num2}相加结果为：{sum}")

# 第二种
print('数字{0}和{1}相加结果为：{2}'.format(num1, num2, sum))
print(f'数字{num1}和{num2}相加结果为：{sum}')

# 第三种   占位符
print("两数之和为 %.1f" %(float(input('输入第一个数字：'))+float(input('输入第二个数字：'))))
print('------------------')


# 输出的方式：表达式语句 print函数 标准输出文件件sys.stdout
# str.format()函数    格式化输出值
print('{0}今天又{1}! '.format('我', '吃得好饱'))
print('{who}希望幸运{how}'.format(who='我', how='满分'))

# repr()或str()函数    将输出的值转成字符串
print(str(1/7))
print(repr('jid'))      # 输出: ‘jid'
print(repr('jis\n'))    # 可以转义字符串中的特殊字符

# str.rjust(num)      将字符串靠右，并在左边填充空格
print(repr(45).rjust(4))
# str.zfill(num)       在数字左边填充0
print('34'.zfill(4))
