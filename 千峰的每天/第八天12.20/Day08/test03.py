"""
3.把下列字典按照年龄和姓名排序并输出到控制台
stus = [
{"name": "张三", "age": 18},
{"name": "李四", "age": 35},
{"name": "王五", "age": 22}]
"""
stus = [
    {"name": "张三", "age": 18},
    {"name": "李四", "age": 35},
    {"name": "王五", "age": 22}]

dict_stus = [{"name": "张三", "age": 18}, {"name": "李四", "age": 35}, {"name": "王五", "age": 22}]
print(dict_stus)

dict_stus.sort(key=lambda x: x["age"])
print(dict_stus)
