"""
csv_reader = csv.reader(fileobj 、 iterable)
可以遍历csv_reader获取fileobj或者iterable对象中所有的内容
"""

import csv

# 创建流对象
file = open("Univ_Ranking_V3.csv", mode="r")
# 创建csv对象，这个对象中包含文件内所有的内容
csv_reader = csv.reader(file)
# 遍历这个对象
for i in csv_reader:
    print(i)
# 关闭流
file.close()
