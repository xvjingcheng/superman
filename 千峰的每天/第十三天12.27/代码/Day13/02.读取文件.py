"""
read        一次读取文件内所有内容
readline    每次读取一行内容
readlines   一次读取全部内容，返回一个列表，每一行当做一个元素
"""

file = open("demo02.txt", mode="r", encoding="utf-8")

# file.write("白日依山尽，黄河入海流。\n")
# file.write("欲穷千里目，更上一层楼。\n")

content = file.read()
# content = file.readline()
# content = file.readlines()

print(content)

file.close()
