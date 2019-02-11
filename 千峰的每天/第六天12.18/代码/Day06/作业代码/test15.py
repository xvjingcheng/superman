"""
15、使用生成器（分别使用iter()和函数实现）
生成斐波那契数列
生成1000年--2000年以内的闰年
"""


def get_fib(y):
    a = 0
    b = 0
    c = 1
    # 1 1 2 3 5 8 13 21
    while a < y:
        b, c = c, b + c
        # 我们需要的是生成器，使用yield记录每一个产生的数据
        yield b


fib = get_fib(10)
print(fib)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))


def get_leap_year():
    for i in range(1000, 2001):
        # 判断是否是闰年
        if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
            # 使用yield记录数据
            yield i


get_leap = get_leap_year()
print(get_leap)
print(next(get_leap))
print(next(get_leap))
print(next(get_leap))
print(next(get_leap))
print(next(get_leap))
print(next(get_leap))
