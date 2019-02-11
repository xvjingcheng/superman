"""
生成器
    无法直接输出生成器里面的内容
    生成器保存的是数据的算法/规则，每一次调用产生一个
    生成器创建使用yield关键字
        函数可以有返回值，返回值返回给调用者
        yield 跟return功能类似，
            return直接返回直观结果
            yield返回给调用者的不是直观结果，是数据存取的算法、规则
"""

generator00 = (x * 2 for x in range(10))
print(generator00)
print(type(generator00))

# for gen in generator00:
#     print(gen)

"""
print(next(generator00))
print(next(generator00))
print(next(generator00))
print(next(generator00))
print(next(generator00))
"""

# print(len(generator00))

i = 0
while i < 5:
    print(next(generator00))
    i += 1


def show():
    a = 0
    b = 1
    c = 0

    while a < 10:
        b, c = c, b + c
        # print(b)
        yield b
        a += 1


fib = show()
print(fib)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))


def add2(a, b):
    # return a + b
    yield a + b


print("*" * 20)

result = add2(3, 5)
print(result)
print(next(result))


def get2():
    for i in range(50):
        yield (i * 2)


result00 = get2()
print(next(result00))
print(next(result00))
print(next(result00))
print(next(result00))
print(next(result00))

print(next(get2()))
print(next(get2()))
print(next(get2()))
print(next(get2()))
print(next(get2()))
