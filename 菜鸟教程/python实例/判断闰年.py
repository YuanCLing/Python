year = input('请输入一个年份：')
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(f'{year}是闰年')  # 整百年能被400整除，闰年
        else:
            print(f'{year}不是闰年')
    else:
        print(f'{year}是闰年')  # 非整百年能被4整除，闰年
else:
    print(f'{year}不是闰年')
