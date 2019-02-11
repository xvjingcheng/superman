def show(name, age):
    print("这个人的名字是%s,年龄是%s岁" % (name, age))


show("Lily", 25)

show(25, "Lily")

show(age=25, name="Lily")

# show(age=26, "Lily")

# 默认情况下，实参和形参的位置是对应的，关键字参数可以改变他们的顺序
# show(25, name="Lily")

with open("aaa.txt", "w", encoding="utf-8") as file:
    file.write("helloworld")
