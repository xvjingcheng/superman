"""
3、模拟车间生产调度，编写回调函数案例
例如：指定某人去执行某项工作
"""


def 修机器(name):
    print("%s被指定去修理机器" % name)


def 做饭(name):
    print("%s被指定去做午饭" % name)


def 调度(name, func):
    return func(name)


调度("老王", 做饭)
