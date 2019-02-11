"""
删除字典内容
    pop(key)
        删除指定的键值对，返回被删除键对应的值
    popitem()
        默认删除最后一个item，返回有该item中key和value组成的元组
    clear()
        清除字典内的所有item
    del dict[key]
        删除指定key对应的item，没有返回值，如果key不存在，报错：KeyError
"""

dict01 = {"username": "dushine",
          "password": 123456,
          "address": "杭州",
          "is_on_work": True,
          "city": ["北京", "深圳", "上海", "湖南"]}

# print(dict01.pop("city"))
"""
print(dict01.popitem())
print(dict01.popitem())
print(dict01.popitem())
print(dict01.popitem())
"""

# dict01.clear()
# print(dict01)

del dict01["city"]
print(dict01)

del dict01["is_on_work"]
print(dict01)

# del dict01[123456]
# print(dict01)
