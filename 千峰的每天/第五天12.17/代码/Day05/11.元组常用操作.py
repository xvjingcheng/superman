"""
元组有一个特征：一旦确定不可更改----元组和元组元素的ID不可改变
增
    没有提供增加元素的方法
删
    没有提供删除的方法,TypeError: 'tuple' object doesn't support item deletion
    可以使用del tuple删除整个对象
改
    元组不可更改，否则报错：TypeError
查
    count
        查看指定元素在元组中的数目，如果没有返回0
    index
        查看指定元素在元组中第一次出现的位置下标，
        如果没有就报错ValueError: tuple.index(x): x not in tuple
排序
    没有提供排序的方法
    可以使用sorted进行排序，但是，得到是一个全新的列表
相加
    元组可以相加，得到一个包含两个元组内容的新元组
"""
tuple00 = (1, 2, 5, 30, 1, 2, 5, 3, 2, 5, 3)
# tuple00[0] = 10
print(tuple00)

# del tuple00
# print(tuple00)
print(tuple00.count(10))

print(tuple00.index(3))

print(max(tuple00))
print(min(tuple00))

print(sorted(tuple00))
str00 = "helloWorld"
print(sorted(str00))

tuple01 = (123, "hello", [1, 2, 3])
# tuple01[0] = 10
print(id(tuple01[2]))
tuple01[2].append(4)
print(tuple01)
print(id(tuple01[2]))

# tuple01[1] = "World"
# print(tuple01)

tuple02 = (456, 789)
tuple03 = tuple01 + tuple02
print(tuple03)

print(id(tuple02))
tuple02 += tuple01
# tuple02 = tuple02 + tuple01
print(id(tuple02))

"""
in/not in
"""
tuple01 = (123, "hello", [1, 2, 3])

is_in = 123 in tuple01
is_not_in = 123 not in tuple01
print(is_in)
print(is_not_in)

is_in = [1, 2, 3] in tuple01
is_not_in = [1, 2, 3] not in tuple01
print(is_in)
print(is_not_in)

# join
list00 = ["a", "b", "c", "d", "e", "f", "g"]
print("\t".join(list00))

print(".".join(tuple01))
