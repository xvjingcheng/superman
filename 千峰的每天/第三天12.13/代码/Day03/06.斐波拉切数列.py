"""
0,1,1,2,3,5,8,13,21,34,55
"""

a = 1
b = 0
c = 1

while a <= 10:
    b, c = c, b + c
    print(b)
    a += 1

str00 = "abcdefg"
index = 0
while index < len(str00):
    print(str00[index])
    index += 1

for w in enumerate(str00, 1):
    print(w)

print("*" * 20)

str00 = "abcdefg"
index = 0
while index < len(str00):
    print(str00[index], index)
    index += 1
print(sum(range(1,101,2)))