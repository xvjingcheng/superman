import calendar

print(calendar.Calendar.firstweekday)

print(calendar.month(2018, 12))
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.calendar(2019))

print(calendar.isleap(2018))
print(calendar.isleap(2020))

print(calendar.February)

print(calendar.FRIDAY)

print(calendar.SUNDAY)

print("hello\0world")

# while True: pass

for i in range(5): print(i)
x, y = 8, 5
if x > y: print("lalala")

from collections import Iterable

a = range(1000)
print(isinstance(a, Iterable))
print(a[1:10])
print(a[-3])

a = (1, 2, 3)
print(list(a))


def add2(a, b):
    print(a + b)


c = add2
c(3, 5)

set00 = {3, 5, add2}
print(set00)

DICT00 = {1:2,2:3}
DICT00.pop(1)
