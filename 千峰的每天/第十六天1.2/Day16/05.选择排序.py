"""
list01 = [1, 2, 4, 6, 4, 34, 57654, 5, 7, 8, 9, 4, 3, 235]
"""
# list01 = [1, 2, 4, 6, 4, 34, 57654, 5, 7, 8, 9, 4, 3, 235]
list01 = [1, 34, 57654, 5, 235]

for i in range(len(list01) - 1, 0, -1):
    # 假设最大元素的下标为0
    max_index = 0
    # 把最大的元素和所有未排序的元素进行比较
    for j in range(1, i + 1):
        if list01[max_index] < list01[j]:
            max_index = j
    list01[max_index], list01[j] = list01[j], list01[max_index]

print(list01)
