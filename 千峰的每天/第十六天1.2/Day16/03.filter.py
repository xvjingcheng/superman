result = filter(None, [True, False])
print(result)
# print(next(result))
# print(next(result))

for r in result:
    print(r)


def get_result(i):
    if i % 2 == 0:
        return True
    else:
        return False


result = filter(get_result, list(range(101)))
for i in result:
    print(i, end="\t")

print()

result = filter(lambda x: x % 2 == 0, list(range(101)))
for i in result:
    print(i, end="\t")

print()
print(list(filter(lambda x: x % 2 == 0, list(range(101)))))

for i in filter(lambda x: x % 2 == 0, list(range(101))): print(i, end="\t")
print()

list01 = [["张三", 18, "不详"], ["李四", 20, "male"]]
result = filter(lambda x: ((x[2] == "male") or (x[2] == "female")), list01)
for i in result:
    print(i, end="\t")


def judge(a, b):
    if a > b:
        return True
    else:
        return False


list02 = [3, 6, 8, 4, 2, 5]
print(sorted(list02, key=abs))

dict_name = {"a": 15, "b": 18, "c": 12, "e": 11}
print(sorted(dict_name, key=lambda x: dict_name[x]))

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print(sorted(students, key=lambda x: x[2]))

print("*" * 20)


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    # def __str__(self):
    #     return "%s,%s,%s" % (self.name, self.grade, self.age)

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10), ]

print(student_objects)
print(sorted(student_objects, key=lambda x: x.age))

dict_students = [{"name": "张3", "age": 20},
                 {"name": "张4", "age": 18},
                 {"name": "张5", "age": 22},
                 {"name": "张6", "age": 16}]
result = filter(lambda x: x["age"] >= 18, dict_students)
print(result)

for r in result:
    print(r)
