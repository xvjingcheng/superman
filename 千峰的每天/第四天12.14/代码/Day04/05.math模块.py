"""
math
    数学模块，封装了很多数学计算方法
    # 天花板数字，向上取整
    print(math.ceil(4.4))
    # 地板数字，向下取整
    print(math.floor(4.8))
"""
import math

# 天花板数字，向上取整
print(math.ceil(4.4))
# 地板数字，向下取整
print(math.floor(4.8))
# help是Python自带的函数，同过help(XXX)可以查看XXX的所有帮助信息
# help(math.floor)
# help(print)
# help(help)
print(math.degrees(10))
print(math.pi)
print(math.pow(2, 3))
# 把2当做基数，求它的指数
print(math.log2(9))
# 前面的参数是结果，后面的参数是基数，求指数
print(math.log(9, 3))
# 获取一个数字的整数和小数部分，返回的是一个元祖，元祖0位是小数，1位是整数部分
print(math.modf(3))
# 返回这个数字的绝对值，返回值类型是float类型
print(math.fabs(-1))
print(math.fabs(-3.3))
print(math.ceil(-3.3))
print(math.floor(-3.3))
# 返回最大公因子(公约数)
print(math.gcd(10, 29))
print(math.gcd(100, 20))
