"""
偏函数
    已经内置了一部分参数
    调用时
        只需要传入一部分参数
"""


def add2(a, b):
    print(a)
    print(b)
    return a + b


def add3(a, b=5):
    return a + b


print(add2(3, 5))
print(add3(3, 5))
print(add3(3))

from functools import partial

add22 = partial(add2, 3, 5)
print(add22)
add22()


