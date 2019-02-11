"""
重写
    overrides method in XXX
    就是子类中，有一个和父类相同名字的方法，在子类中的方法会覆盖父类中的方法
    必须有继承关系 + 方法名相同 --》 覆盖已经继承父类的方法
    方法名                     作用
    父类名.__init__(self)      调用指定父类中的init方法，获取其中定义的属性
                                如果所调用的类的init方法中有参数，调用的时候也要加上参数
    super(类名,self).__init__()调用指定类的父类中的init方法，获取其中定义的属性
                                如果所调用的类的init方法中有参数，调用的时候也要加上参数
    super().__init__()         只能调用一个父类中的init方法，获取其中定义的属性
                                如果所调用的类的init方法中有参数，调用的时候也要加上参数
"""


class DemoFu(object):
    def __init__(self, cook):
        self.KongFu = "天下第一"
        self.cook = cook

    def demo00(self):
        print("我是父类中的方法")


class DemoSon(DemoFu):
    def __init__(self, cure):
        # 轻功是怎样练成的
        self.QingGong = "水上漂"
        self.cure = cure

    def demo00(self):
        print("我是子类中的方法")


# 报错：如果本类继承有父类和爷爷类等更高级的类，在继承顺序中要把辈分最小的那个写在前面，后面也按照这个规则
class DemoGrandSon(DemoSon, DemoFu, object, ):

    def __init__(self):
        # 调用父类中的init方法
        # super(DemoGrandSon, self).__init__()
        # super(DemoSon, self).__init__("苏格兰打卤面")
        # DemoSon.__init__(self)
        # DemoFu.__init__(self)
        # self.NeiGong = "乾坤大挪移"
        # 只能获取父类中父类的init方法
        super().__init__("跌打损伤")

    def demo00(self):
        print("这是孙子类中的方法")


grandSon = DemoGrandSon()
grandSon.demo00()

# C3
print(DemoGrandSon.__mro__)
print(grandSon.QingGong)
# print(grandSon.KongFu)
# print(grandSon.NeiGong)
