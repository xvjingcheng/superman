"""
匿名函数经典用法
    当做参数传递

"""

dict_student = {"周毅": 660, "吴二": 661, "郑三": 659, "王思": 700}
print(sorted(dict_student))

list_student = [{"name": "周毅", "score": 660},
                {"name": "吴二", "score": 661},
                {"name": "郑三", "score": 659},
                {"name": "王思", "score": 700}]
list_student.sort(key=lambda x: x["score"], reverse=True)
print(list_student)
