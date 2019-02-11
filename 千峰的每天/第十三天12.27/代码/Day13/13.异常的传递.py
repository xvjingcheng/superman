"""
异常的传递
    我们调用方法的时候，方法中可能出现错误，
    这个错误或传递到当前运行的主d代码中，需要做异常的处理
    可以再被调用的方法中处理，也可以在主代码中处理
"""
import os


def demo13():
    try:
        os.remove("file")
    except Exception as e:
        print(e)


def get_result(*args):
    result = 0
    for i in args:
        result += i
    return result


while True:
    select = int(input("请输入您的选择"))
    if select == 1:
        # try:
        #     demo13()
        # except Exception as e:
        #     print(e)
        demo13()
    elif select == 2:
        print(get_result(1, 2, 3, 4, 5))
    elif select == 3:
        break
    else:
        print("输入有误")
