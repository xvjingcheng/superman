"""
# 1:表示有票，0表示没票


>练习：<br/>
01.从键盘输入刀子的长度，如果刀子长度没有超过10cm，允许上火车，反之不允许<br/>
02.在控制台输入一个4位数年份，判断它是否是闰年
"""
ticket = 1
if ticket == 1:
    print("有票，可以通过")
else:
    print("请先去买票")

# 闰年的条件：可以被4整除且不能被100整除或者可以被400整除
year = int(input("请输入年份:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("今年是闰年")
else:
    print("这个不是闰年")

year = int(input("请输入年份："))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("今年是闰年")
else:
    print("今年不是闰年")
