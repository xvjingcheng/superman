"""
匿名函数
    没有名字的函数,使用关键字lambda声明
    lambda args1,args2.... :expression
    能访问lambda表达式以外的参数，只能返回一个值
"""
import keyword

print("lambda" in keyword.kwlist)

sum00 = lambda a, b,: a + b
result = sum00(3, 5)
print(result)

sum01 = lambda c, d: print(c + d)
sum01(4, 5)

sum02 = lambda a: [x for x in range(a)]
print(sum02(10))

c = 10
sum03 = lambda a, b: (b, a)
print(sum03(3, 5))

# 能访问lambda表达式以外的参数，只能返回一个值
sum04 = lambda a, b: a + b + c
print(sum04(2, 3))
