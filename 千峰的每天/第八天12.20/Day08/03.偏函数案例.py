"""
偏函数和进制转换
"""
# base=X    表示进制
result = int("123", base=8)
print(result)

# 使用默认参数改变默认进制
def int2(x, base=2):
    result = int(x, base)
    return result


print(int2("0011"))


def int8(x, base):
    result = int(x, base)
    return result


from functools import partial

int88 = partial(int8, base=8)
print(int88)
print(int88("111"))
