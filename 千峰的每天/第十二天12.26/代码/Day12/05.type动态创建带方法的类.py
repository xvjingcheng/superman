"""
type创建带方法的类
    普通方法
        参数列表中至少有一个参数:self
    静态方法
        需要使用@staticmethon修饰，参数列表可以为空
    类方法
        参数列表至少需要一个参数:cls
"""


def show09(self):
    print("show09")


@staticmethod
def show10():
    print("show10")


@classmethod
def show11(cls):
    cls.q = "QQQ"
    print("show11")


Demo09 = type("Demo09", (object,), {"show09": show09})
Demo09.show09("a")
# help(Demo09)
Demo10 = type("Demo10", (object,), {"show10": show10})

# help(Demo10)

Demo10.show10()

demo10 = Demo10()

demo10.show10()

print(demo10.show10 is Demo10.show10)

Demo11 = type("Demo11", (object,), {"show11": show11, "show10": show10, "show09": show09, "q": "qqq"})

# help(Demo11)

print(Demo11.q)
Demo11.show11()
print(Demo11.q)
