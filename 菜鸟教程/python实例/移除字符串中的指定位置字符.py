# 方法1
test_str = "happy ending"
print(test_str)
new_str = ""
for i in range(0, len(test_str)):  # 下标索引
    if i != 2:
        new_str = new_str+test_str[i]
print(new_str)

# 方法2
print(test_str)
new_str = test_str.replace(test_str[2], "", 1)  # 1 不能少，但是为什么？
# 如果没有指定1，就会取代所有的这个字符串
print(new_str)

# 方法3
print(test_str)
print(test_str[:3]+test_str[4:])
