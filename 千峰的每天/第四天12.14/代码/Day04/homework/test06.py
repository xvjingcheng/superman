"""
6.输出小写的 a-z 以及大写的在Z—A
"""
for i in range(65, 91):
    print(chr(i), end="\t")

print()

for i in range(122, 96, -1):
    print(chr(i), end="\t")
