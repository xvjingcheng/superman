"""
3、有三个房间，有九个人
把这九个人随机分配到三个房间
每个房间人数保持一致
"""
import random

name_list = ["张默", "尹相杰", "宁财神", "李代沫", "房祖名", "高虎", "宋冬野", "张耀扬", "满文军"]
room_list00 = []
# list00 =  ["不好","a","还好"]
for i in range(3):
    room_list = random.sample(name_list, 3)
    for name in room_list:
        name_list.remove(name)
    room_list00.append(room_list)
print(room_list00)
