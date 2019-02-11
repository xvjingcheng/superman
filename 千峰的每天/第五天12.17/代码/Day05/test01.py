"""
1、一个整数加上100和268后都是一个完全平方数，请问该数是多少
    开平方之后得到的整数
    正整数  --- 加上100之后的结果
"""
import math

for i in range(-99, 1000000):
    if (math.sqrt(i + 100) % 1 == 0) and (math.sqrt(i + 268) % 1 == 0):
        print(i)
