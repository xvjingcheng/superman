"""
8、编写一个函数，用于判断输入字符串是否由小写字母构成
chr
ord
"""

str00 = input("请输入一个字符串:")


def check_str(str01):
    for s in str01:
        # 获取每一个字符的ASCII码
        str_num = ord(s)
        # flag 标记这个字符串是否符合条件
        flag = True
        if not str_num >= 97 and str_num <= 122:
            flag = False
            break
    return flag


is_True = check_str(str00)
print("这个字符串全是小写字母的结论是%s" % is_True)
