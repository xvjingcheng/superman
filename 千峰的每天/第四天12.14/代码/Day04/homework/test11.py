"""
11.定义两个整数a和b，a和b的取值范围在0-9之间，给出所有符合a+b=12的组合。
"""

for a in range(0, 10):
    for b in range(0, 10):
        if a + b == 12:
            print("a=%d,b=%d" % (a, b))


