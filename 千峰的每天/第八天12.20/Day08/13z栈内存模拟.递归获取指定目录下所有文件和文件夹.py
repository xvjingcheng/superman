import os

"""
栈内存
    存储特点：数据先到栈内存的后弹出，后面到栈内存的先弹出
"""
# 存放所有的文件和文件夹名字
files_list = []


def get_all_files(path):
    # 获取path路径下所有的文件和文件夹，返回一个列表
    file_list = os.listdir(path)
    # print(file_list)
    # 遍历得到的文件列表，判断每一个文件，如果是文件夹就执行递归，如果不是就输出到控制台
    for file in file_list:
        abs_file_path = os.path.join(path, file)
        if os.path.isdir(abs_file_path):
            # 这个是文件夹，继续打开
            # print("文件夹:", abs_file_path)
            get_all_files(abs_file_path)
        files_list.append(abs_file_path)


path = r"D:\workSpace\PycharmProjects\HZ1807"
get_all_files(path)
print(len(files_list))

length = len(files_list)
for i in range(length):
    print(files_list.pop(0))
    # print(files_list.remove(files_list[0]))
