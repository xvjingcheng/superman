"""
__class__
    查看对象的类型，和内建函数type(obj)功能基本相同
"""


class Demo17(object):
    def __init__(self):
        self.v = "vvv"

    def show17(self):
        print("show17")


print(type(Demo17))
print(Demo17.__class__)

print("hello".__class__)

demo17 = Demo17()
print(demo17.__class__)

print(__name__)
