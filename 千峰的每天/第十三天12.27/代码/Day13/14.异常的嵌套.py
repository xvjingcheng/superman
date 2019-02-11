"""
IndexError
ValueError
ZeroDivisionError
FileNotFoundError
异常的嵌套
    如果出现异常，那么这个异常子级的代码讲无法继续运行
    和他平行的那一级可以正常运行
"""

print("代码开始运行")

try:
    print("异常处理的第一层")
    try:
        print(1 / (int(input("请输入一个整数:"))))
        try:
            print(input("请输入一个很长的字符串")[10])
        except Exception as e:
            print(e)
        try:
            print("我是很长字符串下面那句")
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
except Exception as e:
    print(e)

print("代码运行结束")
