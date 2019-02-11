"""
运算符		描述     			实例
+=		加法赋值运算   	c += a	===>   c = c + a
-=		减法赋值运算   	c -= a  ===>   c = c - a
*=		乘法赋值运算   	c*= a	===>   c = c * a
/=		除法赋值运算   	c /= a  ===>   c = c / a
%=		取余法赋值运算   	c %= a	===>   c = c % a
**=		幂法赋值运算   	c **= a	===>   c = c ** a
//=		取整法赋值运算   	c //= a	===>   c = c // a
"""

a = 10
b = 20

a += b
# a = a + b
print(a)
print(b)
a -= b
print(a)

a *= b
print(a)

a /= b
print(a)
print(type(a))

# a %= 3
print(a)

c = 2
d = 5

c **= d
print(c)

c //= d
print(c)

a //= 4
print(a)
