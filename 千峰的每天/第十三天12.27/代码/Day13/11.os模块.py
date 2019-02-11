import os
# 创建文件夹，如果文件夹已经存在：FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。: 'file'
# os.mkdir("file")
# 提示没有？
# os.mknod("demo11.txt")
# help(os.mknod)
# print(os.mknod)

# Remove a file (same as unlink()).
# FileNotFoundError: [WinError 2] 系统找不到指定的文件。: 'demo11.py'
# print(os.remove("demo11.py"))

# Rename a file or directory.
# FileNotFoundError: [WinError 2] 系统找不到指定的文件。: 'demo11.txt' -> 'demo111.txt'
# os.rename("demo11.txt", "demo111.txt")
os.rename("file", "file00")

# Test whether a path exists.  Returns False for broken symbolic links
print(os.path.exists("file0"))

# Return a unicode string representing the current working directory.
print(os.getcwd())

abs_path = os.path.join(r"D:\workSpace\PycharmProjects\HZ1807\Day13", "demo111.txt")
print(abs_path)

print(os.listdir())
