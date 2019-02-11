"""
2. 编写代码实现计算器三角形周长和面积的计算
属性		说明
length_a	第一条边长
length_b	第二条边长
length_c	第三条边长

方法		说明
get_perimeter	获取周长
get_area	获取面积

需求说明:
用户输入边长
判断输入内容是否合法
提示计算方式
返回调用结果
"""

import math


class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        # 预设参数
        self.perimeter = 0
        self.area = 0

    # 判断能否组成三角形
    def judge(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return True
        else:
            return False

    # 获取周长，需要先判断是否能组成三角形
    def get_perimeter(self):
        if self.judge():
            self.perimeter = self.a + self.b + self.c
            return self.perimeter
        else:
            return "无法构成三角形"


    # 获取面积，需要先判断是否能组成三角形
    def get_area(self):
        if self.judge():
            p = self.get_perimeter() / 2
            self.area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
            return self.area
        else:
            return "无法构成三角形"



    # 把对象返回一个字符串
    def __str__(self):
        return "三角形的周长是：%s，面积是：%s" % (self.get_perimeter(), self.get_area())


s = Triangle(3, 4, 5)
print(s)
