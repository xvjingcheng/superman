"""
type创建带继承关系和init方法的类
    在自定义的init方法中可以调用其他类中的init方法，
    把自定义分init方法当做参数放入type函数参数字典中，
    创建实例对象后可以访问到继承的其他类的实例变量
"""


class Demo13(object):
    def __init__(self):
        self.t = "ttt"


class Demo14(object):
    def __init__(self):
        self.u = "uuu"

    def show14(self):
        print("show14")


def __init__(self):
    Demo13.__init__(self)
    Demo14.__init__(self)


Demo15 = type("Demo15", (Demo13, Demo14), {"__init__": __init__})

demo15 = Demo15()
print(demo15.t)
print(demo15.u)

demo15.show14()
