"""
可以交互的调试模块
"""

import pdb


def add2num(a, b):
    c = a + b
    return c


def div2num(a, b):
    # pdb.set_trace()
    c = add2num(a, b) + a - b
    return c


a = int(input("请输入数字a"))
b = int(input("请输入数字b"))
result = div2num(a, b)
print(result)
