"""
2、定义偏函数：生产杯子消耗的时间为2.5小时/个，计算生产指定个数杯子消耗的时间
"""


def 做杯子(num, duration=2.5):
    total_time = num * duration
    return total_time


num = 3
result = 做杯子(num, 2.5)
print("今天我做了%d个杯子，消耗了%s小时" % (num, result))

from _functools import partial

做杯子00 = partial(做杯子, duration=2.5)
print(做杯子00)

num = 4
result = 做杯子00(num)
print("今天我做了%d个杯子，消耗了%s小时" % (num, result))

num = 5
result = 做杯子(num)
print("今天我做了%d个杯子，消耗了%s小时" % (num, result))
