def show01(self):
    print("show01")


@staticmethod
def show001():
    print("show001")


@classmethod
def show0001(cls):
    print("show0001")


# 无法使用关键字赋值
Demo01 = type("Demo01", (object,), {"name": "zhangsan", "show01": show01, "show001": show001, "show0001": show0001})

# help(Demo01)
# 实例/对象/实例对象
demo01 = Demo01()
demo01.show01()
demo01.show001()
demo01.show0001()

print("*" * 20)

Demo01.show01("a")
Demo01.show001()
Demo01.show0001()

# show01("a")
# show001()
# show0001("a")

# hasattr 判断属性是否存在
Demo01.age = 18
print(hasattr(Demo01, "age"))
print(hasattr(Demo01, "age00"))

print(demo01.age)


def say_hello(self):
    print("上午好")


Demo01.say_hello = say_hello

print(hasattr(Demo01, "say_hello"))
demo01.say_hello()

# 增加  查看  修改  删除

Demo01.age = 28
print(demo01.age)

# del Demo01.age
# print(hasattr(Demo01, "age"))
# print(demo01.age)

# delattr == del X.y
delattr(Demo01, "age")
print(hasattr(Demo01, "age"))

"""
@property
装饰器：
    在不改变原函数(代码)的情况下，增加原函数的功能
"""


