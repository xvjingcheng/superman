"""
做一做：定义函数，能够完成输入、输出自己的姓名和年龄，并让函数执行
"""


def show():
    name = input("请输入名字:")
    age = input("请输入年龄:")
    print("这个用户的名字是:%s,年龄是:%s" % (name, age))
    return name, age


show()

"""
函数的分类：
    无参数，无返回值
    有参数，无返回值
    无参数，有返回值
    有参数，有返回值
"""


# 无参数，无返回值
def notice():
    print("天干物燥，小心火烛，三更天啦")


# 有参数，无返回值
def play_movie(movie_name):
    print("准备好，马上开始播放大片:%s" % movie_name)


play_movie("钟馗大战贞子")


# 无参数，有返回值
def LuDaShi():
    info = "CPU:i9 9900K,GPU:2080..."
    return info


print(LuDaShi())


def add2num(a, b):
    return a + b, a * b


print(add2num(3, 5))
add, mul = add2num(5, 8)
print(add, mul)
result = add2num(2, 3)
print(result)
