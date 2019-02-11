"""
最大值 max()
最小值 min()
"""
num_list = [123, 5435, 645632, 313213, 435, 1233, 312, 3]
print(max(num_list))
print(min(num_list))

print(max(313213, 435, 1233, 312, 3))
print(min(313213, 435, 1233, 312, 3))

# 注意：不同类型的元素同处于一个列表中时，不能使用max/min获取最值
num_list = [123, 5435, 645632, 313213, 435, 1233, 312, 3, True, "hello"]
# print(max(num_list))

print(max(313213, 435, 1233, 312, 3, "a"))
