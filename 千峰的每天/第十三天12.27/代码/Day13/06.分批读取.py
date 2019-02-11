"""
read(n)
    每次读取一部分内容,笔记录当前光标的位置，下一次继续往下读
readline(n)
    如果n小于本行内容的数目，则读取该数目的内容
    如果n大于本行内容的数目，则读取本行全部内容，包括换行符
readlines(n)
    每次读取至少一行
    如果n小于本行内容的数目，则读取本行全部内容，包括换行符
    如果n大于等于本行内容的数目，则读取本行和下一行全部内容，包括换行符
"""

file = open("demo06.txt", mode="r", encoding="utf-8")

# file.write("君不见黄河之水天上来，奔流到海不复回，君不见高堂明镜悲白发。。。")
# print(file.read(10))
#
# print(file.readline(350))

# print(file.readlines(33))
"""
print(file.read(5))
print(file.read(5))
print(file.read(5))
print(file.read(5))
"""
"""
print(file.readline(5))
print(file.readline(5))
print(file.readline(5))

print(file.readlines(10))
print(file.readlines(10))
"""

print(file.read())
print(file.read())
print(len(file.read()))


file.close()
