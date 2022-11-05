def merge(arr, l, m, r):
    n1 = m - 1 + 1
    n2 = r - m

    # 创建临时数组
    L = [0] * (n1)
    R = [0] * (n2)

    # 拷贝数据到临时数组 array L[] R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # 归并临时数组到arr[l……r]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # 拷贝 R[] 的保留元素
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    # 拷贝 L[] 的保留元素
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        m = int((l + r) / 2)
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)
