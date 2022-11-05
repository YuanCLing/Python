# 1.注释  2.""" """  3.''' '''

# 使用 反斜杠\ 实现多行语句
total = 1 + 2 + \
        3 + 4 + \
        5
# 在[], {}, () 中的多行语句不需要使用反斜杠 \
total = ['lhash', 'chushfus',
         'cishffh']

# 四种数字类型 int bool float:1.23、3e-2  complex:1+2j

# 字符串
# 反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。 如 r"this is a line with \n" 则 \n 会显示，并不是换行。
# python没有单独的字符类型，一个字符就是长度为1的字符串
# 字符串的截取语法 变量[头下标：尾下标：步长]
# 字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始
# Python 中的字符串不能改变
# 使用三引号(''' 或 """)可以指定一个多行字符串
word = '字符串'
sentence = "这是一个句子"
paragragh = """这是一个段落，
可以由多行组成"""
str = '123456'
print(str)
print(str[0:-1])    # 输出倒数第一个和第二个字符
print(str[0])
print(str[2:5])     # 正数第三个到第五个字符
print(str[2:])      # 第三个及后面所有字符
print(str * 2)      # 输出两次字符串
print(str + '你好')  # 连接字符串
print("-------------------")
print("hello\nworld")
print(r'hello\nworld')  # r 表示输出原始字符串，不发生转义

# 空行也是程序的一部分

# 等待用户输入
input('\n\n按下enter键')

# 同一行中使用多条语句，用 ; 隔开

# print 默认输出换行，实现不换行在变量末尾加上 end=" ":
x = 'a'
y = 'b'
print(x, end=" ")   # 注意“ ”里面的空格，有空格就会两个变量之间输出有空格
print(y, end=" ")

