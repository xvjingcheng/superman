"""
全局变量
    定义在函数外部的变量
    对所有函数起作用
"""

Occupation = "健身教练"
Occupation_list = ["健身教练", "营养师"]


def show():
    name = input("请输入您的名字:")
    age = input("请输入您的年龄:")
    hobby = input("请输入您的爱好:")
    Occupation_list.append("程序员鼓励师")
    print("这个人的名字是:{0},今年{1}岁，平时喜欢{2},他的职业是{3}".format(name, age, hobby, Occupation_list))

    def demo():
        print(name)

    demo()


show()


# print("%s隔壁的小伙小张和他的关系很好" % name)

def show00():
    name = "老李"
    print("%s是一个勤劳勇敢的Python程序员,平时兼职%s" % (name, Occupation_list))


show00()