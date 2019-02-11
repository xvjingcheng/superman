"""
字典概述
    什么是字典
        以键值对的方式存储数据的数据结构，使用{}包裹内容
    定义一个字典
        dict00 = {key1:value1,key2:value2, ... ...}
        值可以是任意类型，键只能是不可变类型
    访问字典
        使用下标访问？不行，报错：KeyError
        使用key访问key对应的值value
"""
dict00 = {"username": "dushine", "password": "123456", "address": "杭州"}
print(dict00)

print(dict00["username"])

for item in dict00:
    print(item, dict00[item])

dict01 = {"username": "dushine", "password": 123456, "address": "杭州", "is_on_work": True,
          "city": ["北京", "深圳", "上海", "湖南"], "birth": (1990, 12, 5),
          "class00": {"class01": "python1801", "class02": "python1802"},
          "phone_num": "189 370 12800"}
print(type(dict01["password"]))
print(dict01["is_on_work"])
print(dict01["city"])
print(dict01["birth"])
print(dict01["class00"])
print(dict01["phone_num"])

dict02 = {"username": "lalala", 1: True, None: "hello", 1.1: 2.2, None: "world", (1, 2, 3): "hello"}
print(dict02)
