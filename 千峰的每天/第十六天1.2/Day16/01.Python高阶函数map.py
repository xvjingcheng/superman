"""
偏函数
"""


def add2num(a, b):
    return a + b


from functools import partial

add2 = partial(add2num, 3)
print(add2(5))
print(map(str, [1, 2, 3, 4]))
result = map(str, [1, 2, 3, 4])
# for m in result:
#     print(m.__class__)

from collections import Iterable, Iterator, Generator

print(isinstance(result, Iterable))
print(isinstance(result, Iterator))

print(next(result))
print(next(result))
print(next(result))
print(next(result))

print(map(int, "9876"))
result = map(int, "9876")
print(next(result))
print(next(result))
print(next(result))

#  练习：将单个字符转换为对应的字面量整数:"1" --> 1  "1234" --> 1234
print(int("1234"))
list00 = ["123", "456", "789"]
# print(int(list00))
for i in list00:
    print(int(i))


def get_int(chr):
    dict00 = {"1": "壹", "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}
    return dict00[chr]


print(get_int("0"))

print(map(get_int, ["1", "6", "9"]))
result = map(get_int, ["1", "6", "9"])
print(next(result))
print(next(result))
print(next(result))

print(isinstance(result, Generator))
