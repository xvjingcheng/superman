"""
偏函数

"""
from functools import partial


def int2(x, base):
    result = int(x, base)
    return result


int22 = partial(int2, base=2)
print(int22)
print(int22("1010"))
