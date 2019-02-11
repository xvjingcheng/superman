class School(object):
    # 定义学校总人数
    schoolNum = 0

    # 初始化对象
    def __init__(self, name):
        self.name = name
        # 学校总人数增加1
        School.schoolNum += 1
        print("新来一个成员：%s，学校目前有%d人" % (self.name, School.schoolNum))

    def say_hello(self):
        print("大家好,我是心来的渣渣辉")


class Stu(School):
    def __init__(self, name, score):
        School.__init__(self, name)
        self.score = score

    def say_hello(self):
        print("我是新来的学员%s，现在的成绩是%s" % (self.name, self.score))


class Teacher(School):
    pass


stu01 = Stu("张三", 700)
stu01.say_hello()
stu02 = Stu("李斯", 660)
stu02.say_hello()
