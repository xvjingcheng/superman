"""
复数类型
    在Python中理解为变量和常量的组合
    在数学中认为是实数和虚数的组合
    在Python中，虚数部分只能使用XXj ,否则会报错：SyntaxError: invalid syntax
        比如：k = 123 + 45j是可以的
              k = 123 + 45i 报错
"""

k = 123j + 45
print(k)
print(k.real)
print(type(k.real))

print(k.imag)
print(type(k.imag))

# h = 67 + 89i
# print(h)
