"""
for i in range(10):
    print(i)
    i -= 1
    print("*" * 20)
    print(i)


i = 0
while i < 10:
    print(i)
    i -= 1
"""

num00 = 12345
str00 = "12345"
list00 = [1, 2, 3, 4, 5]
tuple00 = (1, 2, 3, 4, 5)
dict00 = {1: 1, 2: 2, 3: 3}
set00 = {1, 2, 3, 4, 5}
generator00 = (x for x in range(10))

from collections import Iterable

print(isinstance(num00, Iterable))
print(isinstance(str00, Iterable))
print(isinstance(list00, Iterable))
print(isinstance(tuple00, Iterable))
# 字典默认暴露的key，迭代的时候获取的也是key ---> dict.keys()
print(isinstance(dict00, Iterable))
print(isinstance(set00, Iterable))
print(isinstance(generator00, Iterable))

from collections import Iterator

print(isinstance(num00, Iterator))
print(isinstance(str00, Iterator))
print(isinstance(list00, Iterator))
print(isinstance(tuple00, Iterator))
# 字典默认暴露的key，迭代的时候获取的也是key ---> dict.keys()
print(isinstance(dict00, Iterator))
print(isinstance(set00, Iterator))
print(isinstance(generator00, Iterator))

print(next(generator00))
print(next(list00))
