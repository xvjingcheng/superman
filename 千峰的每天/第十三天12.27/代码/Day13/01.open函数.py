"""
open函数
    file,       :目标文件，可以是相对路径，也可以是绝对路径
    mode='r',   :打开的模式，读取/写入/。。。
    encoding=None,  :写入的编码方式
    newline=None,   :是字符串格式，内容有限制：\n\r\t
"""

file = open(file="demo01.txt", mode="w+", encoding="utf-8")
file.write("00床前明月光，疑是地上霜。\n")
file.write("00床前明月光，疑是地上霜。")
file.close()

file = open(file="demo01.txt", mode="r+", encoding="utf-8")
print(file.read())
file.close()

