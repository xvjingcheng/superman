"""
3、输入某年某月某日，判断这一天是这一年的第几天
"""
year = int(input("请输入年份:"))
month = int(input("请输入月份:"))
day = int(input("请输入日期:"))

day01 = 0
for i in range(1, 12):
    if i == month:
        day01 += day
        print("今天是这一年的%d天" % day01)
        break
    else:
        if i == 4 or i == 6 or i == 9 or i == 11:
            day01 += 30
        elif i == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                day01 += 29
            else:
                day01 += 28
        else:
            day01 += 31
