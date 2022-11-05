num = int(input('请输入一个数字：'))
factorial = 1

if num < 0:
    print('负数没有阶乘')
elif num == 0:
    print('0的阶乘是1')
else:
    for i in range(2, num + 1):
        factorial *= i;
    print(f'{num}的阶乘是{factorial}')
