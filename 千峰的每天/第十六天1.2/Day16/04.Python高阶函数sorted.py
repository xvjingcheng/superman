"""
>总结：
>使用sorted排序后，输出新的列表--返回一个新的对象
>使用sort排序后，还是原来的列表--内部顺序改变了一下
"""
print(sorted("hello", reverse=True))

list00 = [1, 3, 5, 7, 9, 2, 4, 6, 8]
print(sorted(list00))

list02 = [["John", 18], ["Jane", 22], ["David", 16]]
print(sorted(list02, key=lambda x: x[1]))


class Student(object):
    def __init__(self, name, hobby, age):
        self.name = name
        self.hobby = hobby
        self.age = age

    def __str__(self):
        return "%s,%s,%s" % (self.name, self.hobby, self.age)

    def __repr__(self):
        return repr((self.name, self.hobby, self.age))


students_list = [
    Student("John", "抽烟", 18),
    Student("Jane", "喝酒", 38),
    Student("David", "烫头", 32),
]
print(students_list)
print(sorted(students_list, key=lambda s: s.age))
