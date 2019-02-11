"""
__init__
    构造方法(函数)
        构建一个对象
        初始化参数
    调用方式
        无需调用__init__，只要在创建对象是使用类名(参数列表),就能完成自动调用
        参数列表中的参数会自动赋值给__init__方法中的形参
    注意
        这个方法收是继承父类之后自动拥有的，我们是在重写这个方法
    重写
        发在有有继承关系的子存(saveMoney)、取(drawMoney)、查询(checkMoney)、转账(Transfer accounts)、退出(quit)类中
        子类继承父类，拥有父类所有非私有的属性和方法，
        如果子类使用继承自父类的方法不能满足自己的需求，
        可以重写父类的方法
            重写的方法和父类的方法名保持一致
"""


class Bus(object):

    def __init__(self, wheel, color, speed):
        # 属性
        """
        self.wheel = wheel
        self.color = color
        self.speed = speed
        :param wheel:
        :param color:
        :param speed:
        """
        print(id(self))
        self.wheel = wheel
        self.color = color
        self.speed = speed

    def show(self):
        print("这两bus有%d个轮子，颜色是%s，能乘坐30个人，最高能跑到%dKM/H" % (self.wheel, self.color, self.speed))
        print(id(self))


BYD = Bus(6, "紫色", 120)
print(BYD)
BYD.show()
print(id(BYD))
print(id(Bus))
print(BYD.wheel)
print(BYD.color)
print(BYD.speed)

print("*" * 20)

YuTong = Bus(10, "黄色", 100)
print(YuTong)
YuTong.show()
print(id(YuTong))
print(id(Bus))
print(YuTong.wheel)
print(YuTong.color)
print(YuTong.speed)

print("*" * 20)

# 把BYD在内存中指向的地址赠送给JingHua
JingHua = BYD
print(JingHua)
JingHua.show()

JingHua.color = "白色"
print(BYD.color)
