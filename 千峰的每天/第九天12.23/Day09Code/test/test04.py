"""
4、递归计算1--100所有偶数的和
"""


def get_result(num):
    # 判断累加停止的条件
    if num >= 1:
        result = num + get_result(num - 2)
    else:
        result = 0
    return result


print(get_result(100))

# import random

# print(random.randint(1, 100))
