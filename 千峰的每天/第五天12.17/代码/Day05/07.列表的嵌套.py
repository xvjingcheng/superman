"""
列表嵌套
    L = [[列表1],[列表2],[列表3]]
"""
name_list = ["张默", "尹相杰", "宁财神", "李代沫", "房祖名", "高虎", "宋冬野", "张耀扬", "满文军"]
sort_room = [["张默", "尹相杰"], ["宁财神", "李代沫"], ["房祖名", "高虎", "宋冬野"]]
print(sort_room)

for room in sort_room:
    print(room)
    for name in room:
        print(name)

"""
有三个房间
有九个人
把这九个人随机分配到三个房间
    每个房间人数保持一致
"""
name_list = ["张默", "尹相杰", "宁财神", "李代沫", "房祖名", "高虎", "宋冬野", "张耀扬", "满文军"]
# 其实不存在多维列表，多维列表中的每一层列表都是一个单独的元素
sort_room = [[], [], []]

import random

for name in range(len(name_list)):
    sort_room[random.randint(0, 2)].append(name_list[name])

print("*"*20)
print(sort_room)

sort_room = [["张默", "尹相杰"], ["宁财神", "李代沫"], ["房祖名", "高虎", "宋冬野"]]

i = 0
while i < len(sort_room):

    j = 0
    while j < len(sort_room[i]):
        print(sort_room[i][j])
        j += 1

    i += 1
