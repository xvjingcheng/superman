"""
global
    把变量声明为全局变量
    在函数内部如果想修改全局变量，可以在该变量之前使用global修饰，可以达到目的

    声明global变量的函数必须执行之后才能修改变量的值
"""
Occupation = "游泳教练"
globals()

def show():
    global Occupation
    name = "张三"
    age = 18
    hobby = "游泳"
    Occupation = "健身教练"
    print(name, age, hobby, Occupation)


show()

print(Occupation)


def show00():
    global Occupation
    Occupation = "挖掘机司机"


# show00()

print(Occupation)
