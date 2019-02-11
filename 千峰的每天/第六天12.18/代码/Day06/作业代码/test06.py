"""
6、用函数实现交换两个正整数的值，不少于三种方式实现交换
"""


def switch01(a, b):
    # a = 10 b = 20
    result = a + b
    a = result - a
    b = result - a
    return a, b


def switch02(a, b):
    result = a * b
    a = result / a
    b = result / a
    return a, b


def switch03(a, b):
    result = a ^ b
    a = result ^ a
    b = result ^ b
    return a, b


def switch04(a, b):
    return b, a


def switch05(a, b):
    a, b = b, a
    return a, b


"""
10
5
     0000 1010
^    0000 0101
----------------
result 0000 1111

    0000 1111
^   0000 1010
--------------
    0000 0101
"""
a, b = switch01(3, 5)
print(a, b)
a, b = switch02(3, 5)
print(a, b)
a, b = switch03(3, 5)
print(a, b)
a, b = switch04(3, 5)
print(a, b)
a, b = switch05(3, 5)
print(a, b)
