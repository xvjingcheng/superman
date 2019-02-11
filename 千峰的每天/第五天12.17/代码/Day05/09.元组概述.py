"""
元组概述
    创建元组
        tuple00 = (元素1，元素2，元素3，。。。)
        元组壳存放多种类型的数据，可以嵌套，可以存放可变类型的数据
        tuple00 = (1)并不是元组，
        tuple00 = (1，)是元组，
"""
list00 = [1, 2, 3]
print(type(list00))

tuple00 = (1, 2, 3)
tuple05 = ("sds","dffd","zs22f")
print(sorted(tuple05))
print("****")
print(sorted(tuple00))
print(type(tuple00))

list01 = [0]
print(type(list01))

tuple01 = (1)
print(type(tuple01))

tuple01 = (0,)
print(type(tuple01))

tuple02 = (123, True, "hello")
print(tuple02)

tuple03 = (list00, 123, True)
print(tuple03)

tuple04 = ((1, 2, 3), "hello")
print(tuple04)
