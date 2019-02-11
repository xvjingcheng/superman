"""
7.求出1-3+5-7+9-11+13...101的和
"""
sum = 1
i = 1
while (2 * i + 1) <= 101:
    if i % 2 != 0:
        sum -= (2 * i + 1)
    else:
        sum += (2 * i + 1)
    i += 1

print(sum)

sum = 0
index = 1
for i in range(1, 102, 2):
    if index % 2 == 0:
        sum -= i
    else:
        sum += i
    index += 1
else:
    print(sum)
