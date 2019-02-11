"""
不定长参数
       一个函数能够处理比当初声明时更多的参数称为不定长参数，声明时一般不会命名
       很多编程语言中方法有重写@override和重载@overload
       但是Python并不支持多个相同名字的方法存在，所以有的时候我们传入的参数的长度不能确定
       不定长参数很好的解决了这个问题
       不定长参数本质上是一个元组
       如果参数列表中同时有args和*args，那么先满足args的数量，剩余的全部给*args

       *args 中args可以使用其他名字替换，但是不建议这样干，官方使用的全部是args
"""


def add2num(a, b):
    return a + b


def add2num(a, b, c):
    return a + b + c


a = 10
a = 20
print(a)
# print(add2num(3, 5))
print(add2num(2, 3, 5))


def get_sum(*args):
    print(args)
    print(type(args))
    # 这个是求和的函数
    sum00 = 0
    # 遍历用户传入的每一个参数
    for i in args:
        # 累加这些参数
        sum00 += i
    # 返回给调用者计算的结果
    return sum00


sum01 = get_sum(1, 2, 3, 4, 5)
print(sum01)

print("*" * 20)


def get_mul(arg, *aaa):
    result = arg
    print(arg)
    print(aaa)
    for i in aaa:
        result *= i
    return result


print(get_mul(2, 3, 4, 5))
