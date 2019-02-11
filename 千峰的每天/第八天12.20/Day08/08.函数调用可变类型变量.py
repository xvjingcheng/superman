"""
全局变量
    定义在函数外部的变量
    对所有函数起作用

    当函数内部定义的局部变量和外部的全局变量名字相同时，优先使用函数内部的局部变量---->就近原则

    在函数内部修改可变类型变量，变量内容会发生改变，会影响下面函数使用
"""

Occupation_list = ["健身教练", "程序员鼓励师"]
print("全局变量Occupation的ID:%s" % (id(Occupation_list)))


def show():
    name = input("请输入您的名字:")
    age = input("请输入您的年龄:")
    hobby = input("请输入您的爱好:")
    # 这个是show中定义的局部变量，和外部的全局变量Occupation除了名字相同，没有任何关系
    Occupation_list.append("营养师")
    print("show中使用的变量Occupation的ID:%s" % (id(Occupation_list)))
    print("这个人的名字是:{0},今年{1}岁，平时喜欢{2},他的职业是{3}".format(name, age, hobby, Occupation_list))

    def demo():
        print(name)

    demo()


show()


# print("%s隔壁的小伙小张和他的关系很好" % name)

def show00():
    name = "老李"
    print("show00中使用的变量Occupation的ID:%s" % (id(Occupation_list)))
    print("%s是一个勤劳勇敢的Python程序员,平时兼职%s" % (name, Occupation_list))


show00()
