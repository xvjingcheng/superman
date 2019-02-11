"""
5.使用装饰器运行下列代码
def secret():
print("把大象放入箱子里秘籍")
time.sleep(1)
print("第一步:把箱子打开")
time.sleep(1)
print("第二步:把大象放进去")
time.sleep(1)
print("第三步:把箱子关上")
"""
import time


def func(fun):
    def wrapper():
        start_time = time.time()

        fun()

        end_time = time.time()
        total_time = end_time - start_time
        print("消耗总时间:%s" % total_time)

    return wrapper


@func
def secret():
    print("把大象放入箱子里秘籍")
    time.sleep(1)
    print("第一步:把箱子打开")
    time.sleep(1)
    print("第二步:把大象放进去")
    time.sleep(1)
    print("第三步:把箱子关上")


secret()
