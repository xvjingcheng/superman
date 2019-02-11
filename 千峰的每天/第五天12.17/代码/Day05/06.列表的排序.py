"""
列表的排序
    使用sort()方法可以对列表进行排序，默认是自然顺序(ASCII编码)
"""

test_list = ["LiLei", "Lucy", "HanMeiMei", "Poly", "MrWang"]
test_list.sort()
print(test_list)

num_list = [123, 5435, 645632, 313213, 435, 1233, 312, 3]
num_list.sort(reverse=True)
print(num_list)

# UNICODE编码
name_list = ["张默", "尹相杰", "宁财神", "李代沫", "房祖名"]
name_list.sort()
print(name_list)

# sorted()
# print(sorted(num_list))


