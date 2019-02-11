"""
1. 创建学生类,限制某些数据访问
属性	说明
stuNo	学号
name	姓名
sex	性别
age	年龄	18

方法	说明
show()	显示学生信息(所有属性)

需求说明
创建学生对象，设置属性的值，调用自我介绍的方法
"""
"""
传参
    可以使用外部的全局变量
    可以通过__init__方法传入
    可以使用对象调用属性直接赋值
    可以使用类名调用属性赋值
    可以使用set/get之类的方法对属性赋值
"""


class StudentInfo(object):

    def __init__(self):
        self.name = ""
        self.stuNO = "0"
        self.__age = 0
        self.__sex = "男"

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setStuNO(self, stuNO):
        if len(stuNO) != 10:
            print("输入长度有误,请检查后再次输入")
        else:
            self.stuNO = stuNO

    def getStuNo(self):
        return self.stuNO

    def setSex(self, sex):
        if sex == "男" or sex == "女":
            self.__sex = sex
        else:
            self.__sex = "输入有误"
            print("输入的性别不存在")

    def getSex(self):
        return self.__sex

    def setAge(self, age):
        if (age >= 15) and (age < 35):
            self.__age = age
        else:
            print("输入的年龄不正确")

    def getAge(self):
        return self.__age

    def __str__(self):
        return "这个学生的姓名是：%s，学号是：%s，性别：%s，年龄：%s" % (self.name, self.stuNO, self.__sex, self.__age)


stu00 = StudentInfo()
stu00.setName("老王")
stu00.setStuNO("2015010110")
stu00.setSex("男")
stu00.setAge(28)

print(stu00)

stu01 = StudentInfo()
stu01.setName("老王")
stu01.setStuNO("201501011")
stu01.setSex("不详")
stu01.setAge(38)

print(stu01)
