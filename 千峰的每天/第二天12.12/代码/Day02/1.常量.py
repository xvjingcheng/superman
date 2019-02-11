i = 10
print(id(i))

print(id(10))

i = 11
print(id(i))

print(id(11))


a = [1, 2, ['a', 'b']]
b = a
c = a.copy()
a.insert(0, 3)
a[-1].append(3)
print(b)
print(c)
d = {'a':1,'b':2}
d.clear()
d[1] = "a"
d[2] = "b"
print(d)
x = y = z = 1
print(x,y,z)