class Demo18(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_result(self):
        print(__name__)
        return self.a + self.b


# 创建对象
demo0018 = Demo18(5, 8)
# 输出对象的类型
print(type(demo0018))

if __name__ == "__main__":
    demo18 = Demo18(3, 5)
    print(demo18.get_result())
