"""
write       参数是字符串，顺序写入内容，后一次的紧跟前一次的末尾

writeline   参数是列表或者字符串，顺序写入内容，后一次的紧跟前一次的末尾

"""
file = open("demo03.txt", mode="w", encoding="utf-8")
# file.write("唧唧复唧唧，木兰当户织。")
# file.write("不闻机杼声，惟闻女叹息。")

file.writelines("问女何所思，问女何所忆。")
file.writelines("女亦无所思，女亦无所忆。")
file.writelines(['白日依山尽，黄河入海流。\n', '欲穷千里目，更上一层楼。\n'])

file.close()
