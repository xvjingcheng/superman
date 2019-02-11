file = open("dict.txt")

dict_list = file.readlines()

word = input("请输入要查询的英文单词:")

for dict_item in dict_list:
    dict_en = dict_item.split("\t")
    if word.upper() == dict_en[0].upper():
        print(dict_en[0], ": ", dict_en[1])
        break
else:
    print("您查询的单词尚未收录，敬请期待。。。")

file.close()
