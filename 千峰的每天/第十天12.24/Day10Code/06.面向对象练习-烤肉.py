"""
烤牛排:
类:
    类名:
        牛排:
    属性:
        几成熟
            0--3表示生的,4--6表示半生不熟,7--9表示熟了,10及以上表示糊了
        烤制时间
        佐料
            红酒
            胡椒
            ... ...
    行为:
        烧烤
        添加佐料
        __init__()
        __str__()
"""


class CookBeef(object):

    def __init__(self):
        # 几成熟
        self.cook_level = 0
        # 文字描述
        self.cook_string = "生的"
        # 佐料
        self.cendiments = []

    # 烤制的方法，可以传入时间，每一分钟相当于一成熟
    def cook(self, cook_time):
        self.cook_level += cook_time
        # 根据cook_level的数值，改变cook_string的描述信息
        if self.cook_level <= 3:
            self.cook_string = "还在滴血，特别新鲜"
        elif self.cook_level <= 5:
            self.cook_string = "表面熟啦，里面还是生的"
        elif self.cook_level <= 8:
            self.cook_string = "烤制的刚刚好,可以吃啦"
        elif self.cook_level <= 10:
            self.cook_string = "马上就烤焦啦"
        else:
            self.cook_string = "仍了吧，都焦啦"

    # 添加佐料的方法
    def add_cendiments(self, cendiment):
        self.cendiments.append(cendiment)

    def __str__(self):
        return "已经烤制了%s分钟，现在是%s，已添加的佐料有%s" % (self.cook_level, self.cook_string, self.cendiments)


# 创建对象
hui_ling_dun = CookBeef()
print(hui_ling_dun)
# 添加佐料
hui_ling_dun.add_cendiments("黄油")
hui_ling_dun.cook(1)
print(hui_ling_dun)
hui_ling_dun.cook(1)
print(hui_ling_dun)
hui_ling_dun.cook(1)
print(hui_ling_dun)
hui_ling_dun.add_cendiments("盐")
print(hui_ling_dun)
hui_ling_dun.cook(1)
print(hui_ling_dun)
hui_ling_dun.cook(1)
print(hui_ling_dun)
hui_ling_dun.cook(1)
print(hui_ling_dun)


