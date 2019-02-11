"""
输出列表到控制台
    1.直接使用print输出
    2.使用for循环遍历
    3.使用while循环遍历
"""
name_list = ["张三", "李四", "王武", "赵柳", "钱琪"]
print(name_list)

for name in name_list:
    print(name)

print("*" * 20)

i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1

test_list = [2 * x + 1 for x in range(51)]
print(test_list)

# 生成器
test_list = (2 * x + 1 for x in range(51))
print(test_list)
print(next(test_list))
print(next(test_list))
print(next(test_list))
print(next(test_list))
print(next(test_list))

print(sum(range(1, 101)))

for i in range(10): print(i)
