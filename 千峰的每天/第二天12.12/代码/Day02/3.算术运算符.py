"""
+		加  :两个对象相加   	a + b	输出的结果   30
-       减  :两个对象进行相减	a - b 	输出的结果   -10
*       乘  :两个对象进行相乘	a * b	输出的结果   200
/		除  :两个对象进行相除	b / a	输出的结果   2
//		取整:返回商的整数部分	9//2	输出的结果   4	9.0//2.0   输出的结果 4.0
% 		取余:返回除法的余数	b % a   输出的结果   0
**		幂	:返回x的y次幂   	a ** b	10的20次方  输出的结果
"""

a = 10
b = 20
result = a + b
print(result)

c = "hello"
d = "world"
result = c + d
print(result)
# 不同类型的数据可能无法相加
result = str(a) + c
print(result)

# result = a + int(c)
# print(result)

print(a - b)
print(a * b)
print(a / b)

# print(c - d)

e = 5
f = 2

print(e / f)
print(e // f)
print(e % f)

print(e ** f)

g = "1234"
print("这个数字的长度是%d" % len(g))
print("个位数字是：%s，十位数字是：%s，百位数字是：%s，千位数字是：%s" % (g[3], g[2], g[1], g[0]))

print(len(g))
g = int(g)
ge = g % 10
shi = g // 10 % 10
bai = g // 100 % 10
qian = g // 1000
print("个位数字是：%d，十位数字是：%d，百位数字是：%d，千位数字是：%d" % (ge, shi, bai, qian))
