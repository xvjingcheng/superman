"""
2.求100以内的所有素数（素数：一个大于1的自然数，除了1和它本身外，不能被其他自然数整除）
"""

for i in range(2, 101):
    for a in range(2, i):
        if i % a == 0:
            break
    else:
        print(i)
