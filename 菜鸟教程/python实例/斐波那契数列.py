num = int(input('几项？：'))
f1 = 0
f2 = 1
count = 2
if num <= 0:
    print('请输入一个正数')
elif num == 1:
    print('斐波那契数列：1')
else:
    print(f'斐波那契数列：{f1},{f2},', end='')
    while count < num:  # 注意条件
        f = f1 + f2
        print(f, end=',')
        f1 = f2
        f2 = f
        count +=1