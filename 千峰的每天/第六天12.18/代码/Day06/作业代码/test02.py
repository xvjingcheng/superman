"""
2、使用循环生成随机生成10个随机数并保存至列表中。再找出列表中最大值和最小值，输出到控制台
    随机数
        random.randint/random.randrange/random.sample
    循环：while i < 10:   for i in range(10):
    列表添加元素
        append  insert  extend
    列表最大或最小值
        max min
"""

# 创建空列表
import random

list00 = []
# 使用循环添加10个元素
for i in range(10):
    list00.append(random.randint(0, 99))
print(list00)
print(len(list00))

# 获取最大值和最小值
num_max = max(list00)
num_min = min(list00)

print("最大值是:{0},最小值是:{1},最大值是:{0}".format(num_max, num_min))
print("最大值是:", num_max)
