bool01 = True
bool02 = False

print(bool01 + 1)
print(bool02 - 1)

"""
在逻辑判断中，只要不是零或者None，就可以看做True，包括字符串
"""
if None:
    print("TRUE")
else:
    print("False")

print(bool01 + bool02)
print(type(bool01 + bool02))
print(bool01 - bool02)
print(type(bool01 - bool02))
print(bool01 * bool02)
print(type(bool01 * bool02))
print(bool01 / 1)
print(type(bool01 / 1))

print(bool01 and bool02)
print(1 and 0)

print(bool01 & bool02)
print(1 & 0)
