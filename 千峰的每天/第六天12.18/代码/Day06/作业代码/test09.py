"""
9、用户输入一个字符串，
将下标为偶数的字符串提出来合并为一个新的字符串A,
再将下标为奇数的字符提出来合并成为一个新的字符串B，
再将字符串A和B连接起来并且输出
"""


def get_new_word(string):
    # 创建空列表，准备存放奇数位和偶数位的字符
    list_odd = []
    list_even = []
    # 遍历字符串，获取灭一个字符
    for s in string:
        # 根据字符的位置存放在不同的列表中
        if string.index(s) % 2 == 0:
            list_even.append(s)
        else:
            list_odd.append(s)
    # 把列表转化为字符串
    str01 = "".join(list_even + list_odd)
    return str01


str00 = input("请输入一个字符串:")
str01 = get_new_word(str00)
print(str01)

list_odd0 = [s for s in str00[1::2]]
list_even0 = [s for s in str00[::2]]
print(list_even0)
print(list_odd0)
