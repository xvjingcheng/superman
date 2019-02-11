"""
运行中删除属性和方法
    del x.y
    delattr(o, name) ==> del x.y
"""


class Demo19(object):

    def show(self):
        print("show19")


def __init__(self):
    self.a = 110
    self.b = 120
    self.c = 119


# help(Demo19)

Demo19.__init__ = __init__

help(Demo19)

demo19 = Demo19()
print(demo19.a)
print(demo19.b)
print(demo19.c)

Demo19.d = 12315

print(demo19.d)

# 运行中删除属性
del Demo19.d
# print(demo19.d)

# print(Demo19.d)

delattr(demo19, "a")
# print(demo19.a)


Demo19.show("self")
print("*" * 20)

# del Demo19.show
# demo19.show()

delattr(Demo19, "show")
Demo19.show("self")
