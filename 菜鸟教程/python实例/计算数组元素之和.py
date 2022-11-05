from typing import List


def _sum(array: list):
    # 使用内置的 sum 函数计算
    return sum(array)


# 调用函数
arr = []  # 空列表
# 数组元素
arr: list[int] = [12, 4, 4, 5]
# 计算数组的长度
n = len(arr)
ans = _sum(arr)
# 输出结果
print('数组元素之和为', ans)

# 使用for循环
s = 0
for x in range(0, len(arr)):
    s += arr[x]
print(s)
