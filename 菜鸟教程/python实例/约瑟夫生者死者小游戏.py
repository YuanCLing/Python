"""
30 个人在一条船上，超载，需要 15 人下船。

于是人们排成一队，排队的位置即为他们的编号。

报数，从 1 开始，数到 9 的人下船。

如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？
"""
from typing import List, Any

people: list[int | Any] = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11]
# people = []
for x in range(1, 31):
    people[x] = 1
print(type(people))
check = 0   # 数 1-9
i = 1
count = 0   # 下船的人数
while i <= 31:
    if count == 15:
        break

    if i == 31:
        i = 1

    if people[i] == 1:
        check += 1
        if check == 9:
            print(f'{i}下船')
            people[i] = 0
            count += 1
            check = 0
        i += 1
    else:
        i += 1
        continue



