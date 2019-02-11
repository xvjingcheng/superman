"""
python多态
    Python中不存在真正的多态，下面的案例实现Python的伪多态
"""


class F1(object):
    def show(self):
        print("F1方法中的show")


class S1(F1):
    def show(self):
        print("S1方法中的show")


class S2(F1):
    def show(self):
        print("S2方法中的show")


def func(fun):
    fun.show()


# 匿名对象
func(F1())
