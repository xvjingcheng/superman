import time

help(time)

# 获取1970年1月1日到现在的秒数字
print(time.time())

print(time.clock())

# 休眠
time.sleep(0.1)

# 格林尼治时间，和我们的时间差八个时区
print(time.gmtime(time.time()))
print(type(time.gmtime(time.time())))

# 获取当前时区的时间，
print(time.ctime(time.time()))
print(type(time.ctime(time.time())))

# 获取当前时间，返回的一个时间对象，可以继续调用里面的年月日等值
print(time.localtime(time.time()))
print(time.localtime(time.time()))
print(type(time.localtime(time.time())))

print(time.asctime(time.localtime(time.time())))
print(time.asctime())
