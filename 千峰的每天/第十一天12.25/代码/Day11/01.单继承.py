"""
单继承
    抽取所有类共同的特征，形成一个父类，子类继承这个父类获取里面所有公开的内容
    减少重复代码，提高开发效率
"""


class Cat(object):

    def __init__(self):
        self.legs = 4
        self.eyes = 2
        self.__color = "花色"

    def miao(self):
        print("喵喵喵")

    def __demo00(self):
        print("你看不到我")


class BosiCat(Cat):

    def CatchMouse(self):
        print("昨天晚上捉了四只老鼠，他们一家都在这里了")


class BaliCat(Cat):
    weight = "十斤"

    def __init__(self):
        # 如果想重写父类方法的同时还要获取f父类的属性，那么需要调用父类的初始化方法
        Cat.__init__(self)
        # super(BaliCat, self).__init__()
    def show(self):
        print("这是一巨丑的miao")


LittleWhite = BosiCat()
LittleWhite.miao()
print(LittleWhite.eyes)
print(LittleWhite.legs)

LittleWhite.CatchMouse()

print("*" * 20)

LittleBlack = BaliCat()
LittleBlack.show()
# LittleBlack.demo00()
print(LittleBlack.weight)
print(LittleBlack.eyes)
