"""
创建csv对象
csv.writer(fileobj)
放入一个可迭代类型对象，写在一行，每一个元素是一列
csv.writerow(iterable)

放入一个可迭代类型的元素，这个元素中的每一个子元素也必须可迭代
每一个子元素占一行，子元素又会被拆开占据多列，长度取决于自身
csv.writerows(Iterable（Iterable）)

"""
import csv

# 创建流对象
file = open("demo07.csv", mode="w", encoding="utf-8")
# 创建csv对象
csv_writer = csv.writer(file)
# 写入内容
csv_writer.writerow(["a", "b", "c", "d", "e"])

# csv_writer.writerows([[1, 2, 3], "world", "say", "byebye"])
# 关闭流
file.close()
