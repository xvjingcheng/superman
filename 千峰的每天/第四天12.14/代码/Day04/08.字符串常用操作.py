"""
字符串常用操作
    下标：index 从0开始，到len(str)-1
    切片：截取字符串中一部分内容
          str[start:stop:step]
          不包含stop位置的元素
"""
str00 = "床前明月光,疑是地上霜.举头望明月,低头思故乡."

# for s in str00:
#     print(s, end="\t")

print(str00[9])

print(str00[0:6:2])

print(str00[:])
print(str00[::])
print(str00[-1])
print(str00[:-1])
print(str00[::1])
print(str00[::-1])
print(str00[-5:-10:-1])
print(str00[5:-5])
# 切割字符串，以传入的文字切割,可以控制切割的份数
str01 = "唧唧复唧唧，木兰当户织，不闻机杼声，惟闻女叹息。"
print(str01.split("唧", 1))
print(str01)
print(str01.split("闻"))
"""
* find()
* index()
* count()
* replace()
* capitalze()把第一个字符大写
* title()
* swapcase()大小写转换
* startswith()
* endswith()
* lower()
* upper()
* isupper()
* islower()
* ljust()左对齐
* rjust()右对齐
* center()
* zfill()右对齐补0
* strip()去除两端的空字符
* rfind()从右侧查找
* rindex()从右侧查找索引
* partition()以传入内容分割三部分
"""

"""
* find()
* index()
* count()
* replace()
* capitalze()把第一个字符大写
* title()
"""
# 查找指定字符在目标中的位置，可以制定范围，如果没找到返回-1
str02 = "北国风光，千里冰封，万里雪飘，望长城内外，惟余莽莽，大河上下顿失滔滔。"

print(str02.find("，"))
print(str02.find("，", 5))
print(str02.find("，", 5, 8))

# 查找指定字符在目标中的位置，可以制定范围，如果没找到就报错
# index() 查看元素下表
print(str02.index("，"))
print(str02.index("，", 5))
# print(str02.index("，", 5, 8))

# count()查看制定元素在目标中的数目，如果没有就返回0
print(str01.count("唧"))
print(str01.count("唧急急风"))

# replace()替换目标中的元素，可以制定元素个数，如果替换失败，返回原来的字符串
print(str01.replace("唧唧", "jiji"))
print(str01)
print(str01.replace("唧唧", "jiji", 1))
print(str01.replace("唧唧唧唧", "jiji", 1))

# capitalze()把第一个字符大写,其余全部小写
str03 = "life IS short, you need Python"
print(str03.capitalize())

# title() 把每一个单词的首字母大写，其余小写
print(str03.title())

# swapcase()大小写转换
print(str03.swapcase())

# startswith()
print(str03.startswith("life"))
print(str03.startswith("lie"))
# endswith()
print(str03.endswith("Python"))
print(str03.endswith("Py"))
print(str03.endswith("on"))

"""
* lower()   把字母转化为小写
* upper()
* isupper() 返回值类型为bool，判断书否为大写或者小写
* islower()
"""
str03 = "life IS short, you need Python"

print(str03.lower())
print(str03.upper())

print(str03.islower())
print(str03.lower().islower())

"""
* ljust()左对齐
* rjust()右对齐
* center()
* zfill()右对齐补0
"""

str04 = "白日依山尽，黄河入海流。"

print(str04.rjust(20, "*"))
print(str04.ljust(20, "*"))
print(str04.center(20, "*"))
print(str04.zfill(20))

"""
* strip()去除两端的空字符
* rfind()从右侧查找
* rindex()从右侧查找索引
* partition()以传入内容分割三部分
"""
str05 = "   hello   "
print(str05.strip())
print(str01.rfind("唧"))
print(str02.rfind("唧"))

print(str01.rindex("唧"))
# print(str02.rindex("唧"))

str06 = "helloWorld"
print(str06.partition("l"))
print(str06.partition("y"))
