class Review(object):
    def __init__(self):
        self.__age = 0

    def setAge(self, age):
        # 参数合法的情况下给私有变量赋值
        if (age > 0) and (age < 120):
            self.__age = age
        else:
            # 参数不合法
            self.__age = -1

    def getAge(self):
        return self.__age


class ReviewToo(object):
    def __init__(self):
        self.__count = 0

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, value):
        # 参数合法的情况下给私有变量赋值
        if (value > 0) and (value < 120):
            self.__count = value
        else:
            # 参数不合法
            self.__count = -1

    @count.getter
    def count(self):
        return self.__count
