"""
str模块
    使用时不需要导入
    定义字符串可以使用单引号或者双引号包裹，字符串可以包裹一切内容
    字符串一旦确定不可更改？
        变量指向的字符串内容一旦改变，那么他在在内存中指向的位置也随之发生改变
"""
str00 = "hello"
str01 = "True"
str02 = "None"

print(str00)
print(str01)
print(type(str01))
print(str02)

str03 = "hello"
print(str03)
print(id(str03))
str03 = str03 + "world"
print(str03)
print(id(str03))

print("%s" % str03)
print("hello{first}".format(first="world"))
print("hello{}".format("world00"))
print("{0}".format("world00"))
print("{0}{1}".format("world00", "hello"))
print("{0}{1}{0}".format("world00", "hello"))

# 字符串输入使用input()，输入任何内容返回的结果都是字符串
str04 = input("请输入True或者False")
str04 = bool(str04)
print(type(str04))
print(type(str04))

