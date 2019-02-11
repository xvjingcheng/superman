"""
del
    析构方法(函数)

    作用
        删除一个对象是会自动调用

"""


class Track(object):

    def __init__(self, weight, speed):
        self.weight = weight
        self.speed = speed

    def show(self):
        print("刚刚看到一辆卡车,载重是%d顿,时速%d" % (self.weight, self.speed))

    def __del__(self):
        print("%s被删除啦" % self)


import sys

JieFang = Track(10, 100)
JieFang.show()
print(JieFang)
# 增加一条引用
JieFang414 = JieFang

print(sys.getrefcount(JieFang))
# 删除一条引用
del JieFang

print(sys.getrefcount(JieFang414))

print("hello")

DongFeng = Track(30, 120)
DongFeng.show()
print(DongFeng)
print("world")
#author: 叛军
import datetime
import time
dtstr = str(input('Enter the datetime:(20151215):'))
dt = datetime.datetime.strptime(dtstr, "%Y%m%d")
another_dtstr =dtstr[:4] +'0101'
another_dt = datetime.datetime.strptime(another_dtstr, "%Y%m%d")
print (int((dt-another_dt).days) + 1)