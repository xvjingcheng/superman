"""
冒泡排序
    相邻的两个元素比较，大的上升，小的下降
"""

# list01 = [1, 2, 4, 6, 4, 34, 57654, 5, 7, 8, 9, 4, 3, 235]
list01 = [1, 34, 57654, 5, 235]

for i in range(len(list01) - 1, -1, -1):
    for j in range(0, i):
        if list01[j] > list01[j + 1]:
            list01[j], list01[j + 1] = list01[j + 1], list01[j]

print(list01)
