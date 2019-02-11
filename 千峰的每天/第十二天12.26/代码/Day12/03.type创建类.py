"""
type(object_or_name, bases, dict)
    type()可以创建一个类
        object_or_name :表示：类名
        bases 表示继承
        dict 表示属性和方法,属性是类属性,调用属性获者方法时，要和key名称保持一致
"""

print(type("Demo05", (object,), {"a": "aaaa"}))
print(type(type("Demo05", (object,), {"a": "aaaa"})))


def show(self):
    print("demo05")


Demo05 = type("Demo05", (object,), {"a": "aaaa", "show00": show})

demo05 = Demo05()
print(demo05)
print(demo05.a)
demo05.show00()

print(Demo05.a)
