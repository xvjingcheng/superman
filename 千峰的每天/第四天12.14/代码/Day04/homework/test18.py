"""
18.一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
第一次落下   100     50
第二次落下   50      25
第三次落下   25      12.5

"""
height = 100
sum00 = 0
for i in range(10):
    sum00 += (2 * height)
    height = height / 2
print(height, sum00 - 100)
