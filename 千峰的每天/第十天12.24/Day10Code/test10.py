"""
10、使用递归的方式打印九九乘法表
"""


def di_gui99(num):
    if num > 1:
        di_gui99(num - 1)
        for i in range(1, (num + 1)):
            print("%d * %d =%d" % (i, num, i * num), end="\t")
        print()
    else:
        print("1 * 1 = 1")


di_gui99(9)
