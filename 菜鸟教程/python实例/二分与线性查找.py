# 二分查找
def binary_search(arr, l, r, x):
    if r >= 1:
        mid = int((r + l) / 2)

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1


# 线性查找
def search(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1
