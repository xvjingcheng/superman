"""
优秀 >= 90 < 120
良好 >= 80 < 90
一般 >= 70 < 80
及格 >= 60
不及格 < 60
"""
score = int(input("请输入成绩（0--120）:"))
if score > 120:
    print("成绩有误")
elif score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("一般")
elif score >= 60:
    print("刚好及格")
elif score >= 0:
    print("不及格")
else:
    print("输入的成绩有误")
