"""
float
    小数类型
        正小数和负小数
        表示范围比int类型要大一些
        在Python中小数只有float一种类型
        float类型数据无论使用什么计算返回结果都还是float类型
        可以使用int()强制装换为整数，但是小数点后面的数据后消失
"""

f1 = 2.2
f2 = 4.6
print(f1 + f2)
print(type(f1 + f2))
print(f1 - f2)
print(type(f1 - f2))
print(f1 * f2)
print(type(f1 * f2))
print(f1 / f2)
print(type(f1 / f2))
print(f2 / f1)
print(type(f2 / f1))

print(int(f2))
print(str(f1 + f2))
