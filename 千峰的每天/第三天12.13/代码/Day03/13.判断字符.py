"""
随机产生一字符，并输出，判断：如果为大写字母则输出“大写字母”；如果为小写字母则输出“小写字母”；否则怎输出“其他字符”；
"""
import random

word = random.randint(0, 127)

if (word >= 65) and (word <= 90):
    print("这是一个大写字母：%s" % chr(word))
elif (word >= 97) and (word <= 122):
    print("这是一个小写字母：%s" % chr(word))
else:
    print("这个是其他字符")
