def chr_int(chr):
    return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7}[chr]


list01 = ["1", "3", "5"]

result = map(chr_int, list01)

print(result)
# print(type(result))
# print(list(result))
print(type(next(result)))
print(next(result))

# null None

a = 5
b = 3
print(int(a / b))

print(a // b)

# return "hflkadhflkadjsfljdsfl"
# print "fhkdshfkjashfdk"

print("hfkjsahfkjsdhf")

# print(1 > "a")

print(0b1010)
print(0o1010)
# print(01010)

print()
# byte short int long float double char bool
print(chr(97))
print(type(chr(97)))
print(chr(97).__class__)

try:
    print(type(0b1010))
    print(bytes("hello", encoding="utf-8"))
    print(b"hello")

except TypeError as e:
    print(e)

# print(range())

print(list(range(10)))

print([x for x in range(10)])

print(sum(range(101)))

data01 = [["姓名", "年龄", "爱好"], ["xiaoming", 25, "无"], ["laowang", 30, "写代码"]]


def get_name(var):
    if var == "无":
        return False
    else:
        return True


for info in data01:
    result = filter(get_name, info)
    print(list(result))