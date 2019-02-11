"""
8.求出1-1/2+1/3-1/4…..1/100的和
"""

result = 0
index = 1
for i in range(1, 101):
    if index % 2 == 0:
        result -= 1/i
    else:
        result += 1/i
    index += 1
else:
    print(result)
