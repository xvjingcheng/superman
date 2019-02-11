"""
13.随机生成一个五位以内的数，然后输出该数共有多少位，每位分别是什么？
"""

import random



number = random.randint(0, 99999)
print(number)
print("改数字共有%d位" % (len(str(number))))
digit = str(number)
i = 1
while i <= len(digit):
    for temp in digit:
        print("第%d位数字是：%s" % (i, temp))
        i += 1


number = str(random.randint(0, 99999))
print(number)
for i in enumerate(number, 1):
    print(i)

