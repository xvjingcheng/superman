import os

"""
os模块
    是对文件和文件夹执行操作的一个模块
"""
"""
# 获取当前文件路径
print(os.getcwd())
print(os.path.exists("D:\workSpace\PycharmProjects\HZ1807\Day008"))

print(os.path.isdir("D:\workSpace\PycharmProjects\HZ1807\Day08"))

print(os.path.isfile(r"D:\workSpace\PycharmProjects\HZ1807\Day08\01.偏函数.py"))

print(os.listdir("D:\workSpace\PycharmProjects\HZ1807"))
"""

count = 0


def get_all_files(path):
    # 确保我们每一次修改的都是同一个count
    global count
    # 获取path路径下所有的文件和文件夹，返回一个列表
    file_list = os.listdir(path)
    # print(file_list)
    # 遍历得到的文件列表，判断每一个文件，如果是文件夹就执行递归，如果不是就输出到控制台
    for file in file_list:
        abs_file_path = os.path.join(path, file)
        if os.path.isdir(abs_file_path):
            # 这个是文件夹，继续打开
            print("文件夹:", abs_file_path)
            get_all_files(abs_file_path)
        else:
            if abs_file_path.endswith(".py"):
                print("\t文件:", abs_file_path)
                count += 1


path = r"D:\workSpace\PycharmProjects\HZ1807"
get_all_files(path)
print(count)
