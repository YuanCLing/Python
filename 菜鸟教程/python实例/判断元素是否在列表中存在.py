test_list = [1, 2, 4, 45]

print("查看 4 是否在列表中（使用循环）：")
for i in test_list:
    if i == 4:
        print("存在")

print("查看 4 是否在列表中（使用 in 关键字）：")
if 4 in test_list:
    print('存在')

print("查看 4 是否在列表中（使用 count（）函数：")
if test_list.count(4) <= 0:
    pass
else:
    print('存在')
