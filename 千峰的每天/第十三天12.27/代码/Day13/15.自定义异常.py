class ShortInputException(Exception):
    def __init__(self, length):
        self.length = length
        self.atLeast = 6

    def __str__(self):
        return "ShortInputException: 最小长度要求是6,,您输入的是%d" % self.length


try:
    password = input("请输入密码:")
    if len(password) < 6:
        # raise 抛出异常
        raise ShortInputException(len(password))
except ShortInputException as e:
    print(e)
else:
    print("密码长度合法")


class Model:
    def __init__(self,x):
        self.x=x

    def __add__(self, other):
        return  Model(self.x-other.x)
    def __str__(self):
        return ("两个对象相加的值是{x}".format(x=self.x))

a=Model(5)
b=Model(7)
print(a+b)