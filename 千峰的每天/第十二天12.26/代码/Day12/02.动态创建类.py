"""
生成的类不能提前预知
函数的返回值是一个类对象，根据用户传入的参数，判断后返回对应的类
--动态生成类
"""


def choose_name(name):
    if name == "haha":
        class HaHa(object):
            pass
        return HaHa
    elif name == "heihei":
        class HeiHei:
            pass
        return HeiHei
    else:
        return "没有"


print(choose_name("haha"))

print(type(choose_name("haha")))
print(type(type))
