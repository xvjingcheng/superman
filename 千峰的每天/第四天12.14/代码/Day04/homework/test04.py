"""
4.求100~1000之间的所有能被5和6整除的整数，每行显示5个
"""
count = 0
for i in range(100, 1001):
    if i % 5 == 0 and i % 6 == 0:
        print(i, end="\t")
        count += 1
        if count % 5 == 0:
            print()
