list01 = [1, 2, 4, 6, 4, 34, 57654, 5, 7, 8, 9, 4, 3, 235]

for i in range(len(list01) - 1, 0, -1):
    # print(list01[i])
    index = 0
    for j in range(1, i+1):
        if list01[j] > list01[index]:
            index = j
    list01[i], list01[index] = list01[index], list01[i]

print(list01)

list01 = [1, 2, 4, 6, 4, 34, 57654, 5, 7, 8, 9, 4, 3, 235]
for i in range(0, len(list01)):
    for j in range(0, i):
        if list01[j] > list01[j+1]:
            list01[j], list01[j+1] = list01[j+1], list01[j]
print(list01)
