"""
1、应用----批量修改文件名（重命名）
例如：
demo01.txt
demo02.txt
demo03.txt
demo04.txt
demo05.txt
demo06.txt
修改为:
demo01 -[XX出品]  .txt
demo02 -[XX出品] .txt
demo03 - [XX出品].txt
demo04 - [XX出品].txt
demo05 - [XX出品].txt
demo06 - [XX出品].txt
"""
import os

# 获取所有文件名
path = r"E:\file00"
file_list = os.listdir(path)
# 遍历这些文件，获取文件名和后缀名
for name in file_list:
    # 获取绝对路径
    file_abs_name = os.path.join(path, name)
    # 判断是否是文件
    if os.path.isfile(file_abs_name):
        # 获取最后一个点的位置
        index = file_abs_name.rfind(".")
        # 获取文件名
        file_name = file_abs_name[0:index]
        # 获取后缀名
        file_suffix = file_abs_name[index:]
        # 拼接新的文件名字
        file_new_name = file_name + " - [XX出品]" + file_suffix

        # 修改文件名--文件必须是绝对路径
        os.rename(file_abs_name, file_new_name)

str00 = "demo01.demo01.demo01.txt"
print(str00.replace(".", "[千锋出品]."))

file = open("demo00.txt", mode="w", encoding="utf-8")
file.close()

with open("demo00.txt", mode="w", encoding="utf-8") as file:
    path
