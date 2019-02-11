"""
偏函数
    偏： 以偏概全的偏
        函数中已经定义了一部分参数
        更加方便和准确的调用函数
"""

from functools import partial


def add2(a, b):
    result = a + b
    return result


result = add2(3, 5)
print(result)

# 创建一个偏函数，传入函数和其中一部分参数
add5 = partial(add2, 5)

print(add5)
# 调用偏函数，获取返回值：返回值是偏函数中原函数的返回值
result = add5(3)
