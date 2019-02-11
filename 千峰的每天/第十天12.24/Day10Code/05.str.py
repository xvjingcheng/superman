"""
str
    字符串
    把对象转换为字符串
    输出对象的时候直接输出返回的内容就行
    把计算机能识别的内容转换为我们能识别的内容

repr
    把人类能识别的内容转换为计算机识别的内容
"""
import time


class MoToBike(object):

    def __init__(self, displacement, speed):
        self.displacement = displacement
        self.speed = speed

    def show(self):
        print("这辆摩托车的排量是:%s,最高时速是:%dKM/H" % (self.displacement, self.speed))

    def __str__(self):
        return "这辆摩托车的排量是:%s,最高时速是:%dKM/H" % (self.displacement, self.speed)

    """
       def __del__(self):
        for i in range(5, 0, -1):
            time.sleep(0.1)
            print("道奇还有%d秒就被干掉啦" % i)

        print("道奇被干掉啦")
    """



DaoQi = MoToBike(6.0, 666)
# DaoQi.show()

print(DaoQi)

import datetime

now = datetime.datetime.now()
print(now)
print(type(now))
print(str(now))
print(type(str(now)))

print(repr(now))

print(eval(repr(now)))
