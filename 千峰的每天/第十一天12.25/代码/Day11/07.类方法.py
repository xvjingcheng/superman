"""
类方法
    使用@classmethod修饰的方法，参数中必须有cls
    类方法可以直接使用类名调用
    类不能直接调用实例方法
        为什么类对象不能直接调用实例属性/方法
        类属性加载的时机早于实例对象
    在类方法中可以修改类属性，修改的时机是类方法调用的时候，后面调用的都是修改之后的值
"""
"""
静态方法
    使用@staticmethod修饰的方法
    可以使用类对象直接调用，
    参数列表中可以不放任何参数，
    也可以在调用时传入参数
    可以有返回值，也可以没有
"""


class ClassRoom(object):
    height = 3

    def __init__(self):
        self.area = 60
        self.location = "旺田"

    @staticmethod
    def decorate(height00):
        print("hahaha")
        # print("本房间的高度是%d" % height00)
        return "heiheihei"

    @classmethod
    def show(cls):
        print("本教室位置与杭州市江干区九堡镇牛田村旺田大酒店四楼")
        print("本房间的高度是%d" % cls.height)
        return "lalala"

    def desc(self):
        print("这里是普通的描述信息")

    @classmethod
    def show00(cls, num):
        print("本教室位置与杭州市江干区九堡镇牛田村旺田大酒店四楼00000000000")
        print("本房间可以容纳%d人" % num)
        cls.height = 5
        return "lalala"

ClassRoom.height = 15
# ClassRoom.desc()
ClassRoom.show()

phone1000 = ClassRoom()
phone1000.show()
phone1000.desc()
print("*" * 20)

ClassRoom.decorate(5)
phone1000.decorate(5)
print(ClassRoom.show())
print(ClassRoom.decorate(5))

ClassRoom.show00(50)

print("=" * 20)

# 在类方法中修改类属性
ClassRoom.show()
ClassRoom.show00(50)
ClassRoom.show()