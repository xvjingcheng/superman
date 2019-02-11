"""
初始值
while 判断条件:
    循环体
    条件控制语句

"""

i = 0
while i < 10:
    print("我第%d次想你。。。" % i)
    # 条件控制语句
    i = i + 1


i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1

print(sum)

# if...else


