import keyword

print(keyword.kwlist)
print(type(keyword.kwlist))
key_list = ['lambda', 'nonlocal', 'not', 'or', 'pass', 'raise']

"""
定义列表：
    列表名称 = [元素1,元素2,元素3, ......]
    列表长度可以看做是无限制
    列表中存放的元素可以是不同类型
"""
# name_list
# nameList
# NameList
name_list = ["张三", "李四", "王武", "赵柳", "钱琪"]
num_list = [1, 22, 33, 44, 555, 66, 789]
bool_list = [True, False, True]
print(name_list)
print(num_list)
print(bool_list)

test_list = ["张三", 18, False]
print(test_list)

test_list = [name_list, num_list, bool_list]
print(test_list)

test_list = [None]
print(len(test_list))
print(test_list)
