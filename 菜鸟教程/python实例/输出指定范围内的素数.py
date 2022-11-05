import math
lower = int(input('输入区间下界：'))
upper = int(input('输入区间上界：'))
prime_count = 0
for num in range(lower, upper + 1):  # 需要+1，上界在range里面不包括
    if num > 1:
        for i in range(2, int(math.sqrt(num))+1):
            if (num % i) == 0:
                break
            if i == int(math.sqrt(num)):
                print(num)
                prime_count += 1
    else:
        print(num)
        prime_count += 1
print(f'一共有{prime_count}个素数')
