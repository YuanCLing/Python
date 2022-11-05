import cmath
# 正数
num = float(input('请输入一个数字（正数）：'))
num_sqrt = num**0.5
print(f'{num}的平方根是{num_sqrt}')

# 实数和复数     导入复数数学模块
num = int(input('请输入一个数字（实数、负数也可以）：'))
num_sqrt = cmath.sqrt(num)
print(f'{num}的平方根是{num_sqrt}')  # 为什么这种输出方式才可以
# 输出的是 复数形式
