"""
4.把下列内容写成字典("00:16.00":"今天我寒夜里看雪飘过")，按照时间排序：
[00:00.00]Beyond：海阔天空
[01:40.00][00:16.00]今天我寒夜里看雪飘过
[01:48.00][00:24.00]怀著冷却了的心窝飘远方
[01:53.00][00:29.00]风雨里追赶
[01:57.00][00:33.00]雾里分不清影踪
[02:00.00][00:36.00]天空海阔你与我
[02:03.00][00:39.00]可会变(谁没在变)
"""

dict_lrc = [{"time": "00:00.00", "sing_word": "Beyond：海阔天空"},
            {"time": "01:53.00", "sing_word": "风雨里追赶 "},
            {"time": "01:48.00", "sing_word": "怀著冷却了的心窝飘远方"},
            {"time": "01:40.00", "sing_word": "今天我寒夜里看雪飘过"},
            {"time": "01:57.00", "sing_word": "雾里分不清影踪"}]

print(dict_lrc)
dict_lrc.sort(key=lambda x: x["time"])
print(dict_lrc)
