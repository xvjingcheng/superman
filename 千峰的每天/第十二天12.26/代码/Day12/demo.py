"""

"""


class Demo01(object):
    def __init__(self):
        self.a = "a"
        self.b = "b"

    def demo01(self):
        print("demo01")


class Demo02(object):
    def __init__(self):
        self.c = "c"
        self.d = "d"

    def demo02(self):
        print("demo02")


class Demo03(Demo01, Demo02):
    e = "EEEE"

    def __init__(self):
        Demo01.__init__(self)
        Demo02.__init__(self)
        # super(Demo03, self).__init__()
        # super().__init__()

    def demo01(self):
        Demo03.e = "eeee"
        print("demo01+demo03")

    def demo02(self):
        print("demo02+demo03")


demo03 = Demo03()
print(Demo03.e)
demo03.demo01()
print(Demo03.e)
demo03.demo02()

print(demo03.a)
print(demo03.b)
print(demo03.c)
print(demo03.d)

print("*" * 20)


class Demo16(object):
    __slots__ = ("name", "age")

    def __init__(self):
        self.__count = 0

    """
    
    """

    @property
    def count(self):
        print("property被调用")
        return self.__count

    @count.setter
    def count(self, value):
        if isinstance(value, int):
            self.__count = value
        else:
            print("error")

    """
    @count.getter
    def count(self):
        print("getter被调用")
        return self.__count
    """


demo16 = Demo16()
# demo16.count = 100
demo16.count = "100"
print(demo16.count)

print(Demo16.name)
