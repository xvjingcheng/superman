"""
运算符	逻辑表达式      描述     示例
and		x and y 	布尔“与”  如果x为false，x and y  返回false，否则返回y的计算值
or      x or y  	布尔“或”  如果x为True ，返回True 反之返回y的计算值
not		not x 		布尔“非”  如果x为True，返回的False，如果False返回的True
"""

"""
True and False  ==  False
False and True  ==  False
True and True   ==  True
False and False ==  False
"""
"""
True  or  False  ==  True
False or  True   ==  True
True  or  True   ==  True
False or  False  ==  False
"""
a = True
b = False

print(a and b)
print(a or b)

print(a)
print(not a)

"""
&
|
"""
print("*" * 20)
print(a & b)
print(a | b)
