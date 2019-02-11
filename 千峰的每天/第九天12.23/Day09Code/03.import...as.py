"""
import... as
    把导入进来的模块或者函数重命名
        有的是因为函数名/模块名太长
        有的是因为不认识
        改成自己认识的更好用
    一旦使用as把模块或者函数重命名之后，原来的名字在本文件中将不再生效
"""

from functools import partial as pian_han_shu


def add2(a, b):
    return a + b


pian = pian_han_shu(add2, 2)
print(pian(5))

# 一旦使用as把模块或者函数重命名之后，原来的名字在本文件中将不再生效
# add22 = partial(add2, 5)


