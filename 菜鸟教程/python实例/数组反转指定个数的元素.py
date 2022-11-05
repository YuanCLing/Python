"""
定义一个整型数组，并将指定个数的元素翻转到数组的尾部。

例如：(ar[], d, n) 将长度为 n 的 数组 arr 的前面 d 个元素翻转到数组尾部。
"""


# 方法1
def left_rotate1(array, d, n):
    for i in range(d):
        left_rotate_by_one(array, n)


def left_rotate_by_one(array, n):
    temp = array[0]
    for i in range(n - 1):
        array[i] = array[i + 1]
    array[n - 1] = temp


def print_array(array, size):
    for i in range(size):
        print(f'{array[i]}', end=' ')


array = [1, 2, 3, 4, 5, 6, 7]
left_rotate1(array, 2, 7)
print_array(array, 7)


# 方法3
def reverse_array(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1


def left_rotate2(arr, d):
    n = len(arr)
    reverse_array(arr, 0, d-1)
    reverse_array(arr, d, n-1)
    reverse_array(arr, 0, n-1)

print()
array = [1, 2, 3, 4, 5, 6, 7]
left_rotate2(array, 2)
print_array(array, 7)


# 方法2 列表的切片+拼接
def reverse_array_by_slices(arr, d):
    return arr[d:] + arr[:d]


print()
array = [1, 2, 3, 4, 5, 6, 7]
print(reverse_array_by_slices(array, 2))
# 这样直接输出，结果是   [3, 4, 5, 6, 7, 1, 2]
