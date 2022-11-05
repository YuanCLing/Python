# 方法1
arr = list(map(int, input("请输入数组：").split()))
arr.insert(0, arr.pop())
arr.append(arr.pop(1))
print(arr)
# map 内置函数


# 方法2
def swap_list(new_list):
    new_list[0], new_list[-1] = new_list[-1], new_list[0]  # ???
    return newList


newList = [1, 2, 3]
print(swap_list(newList))