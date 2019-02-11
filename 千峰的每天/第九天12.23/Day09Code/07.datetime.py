import datetime
import time

# help(datetime)

now = datetime.datetime.now()

print(datetime.datetime.time(now))

print(datetime.date.ctime(now))

# 获取当前时间
print(now)
print(type(now))

# 获取当前时间
print(datetime.datetime.today())

# 获取格林尼治时间
print(datetime.datetime.utcnow())
# 获取包含年月日时分秒等时间的元组
print(datetime.datetime.utctimetuple(now))

# 获取今天是本周的第几天
print(datetime.datetime.isoweekday(now))
