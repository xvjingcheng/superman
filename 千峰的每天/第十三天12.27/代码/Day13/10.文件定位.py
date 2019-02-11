file = open("demo10.txt", mode="r+", encoding="utf-8")

# print(file.read())

file.seek(2676)
print(file.read())
print(file.tell())

file.close()
