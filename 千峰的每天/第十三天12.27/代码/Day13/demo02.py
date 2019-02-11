class ShortInputException(Exception):
    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast

    def __str__(self):
        return "ShortInputException:输入的长度是%d,长度应该大于%d" % (self.length, self.atleast)


# aa = ShortInputException()

def main():
    try:
        str = input("请输入....")
        if len(str) < 3:
            raise ShortInputException(len(str), 3)
    except ShortInputException as result:
        # print("ShortInputException:输入的长度是%d,长度应该大于%d" % (reslut.length, reslut.atleast))
        print(result)
    else:
        print("没有异常的发生")


main()