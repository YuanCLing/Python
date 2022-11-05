"""
A、B、C、D、E 五人在某天夜里合伙去捕鱼，到第二天凌晨时都疲惫不堪，于是各自找地方睡觉。

日上三杆，A 第一个醒来，他将鱼分为五份，把多余的一条鱼扔掉，拿走自己的一份。

B 第二个醒来，也将鱼分为五份，把多余的一条鱼扔掉拿走自己的一份。 。

C、D、E依次醒来，也按同样的方法拿鱼。

问他们至少捕了多少条鱼?
"""
# 求至少捕了多少条鱼，从小递增，判断是否满足，满足则退出循环


"""def main():
    fish = 1
    while True:
        total, enough = fish, True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1)  //  5 * 4
            else:
                enough = False
                break
        if enough:
            print(f'总共有{fish}条鱼')
            break
        fish += 1


if __name__ == '__main__':
    main()"""

fish = 1
while True:
    total = fish  # 不能写成total=0，因为 -1 不能取模！！！
    enough = True
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) / 5 * 4  # 剩下的的鱼
        else:
            enough = False
            break
    if enough:
        print(f'总共有{fish}条鱼')
        break  # 跳出while循环
    fish += 1

print(type(total))
print(type(enough))
