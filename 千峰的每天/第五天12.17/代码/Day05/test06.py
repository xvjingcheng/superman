"""
6、现有字符串word = "ghSk 45s Df,9 87.fs sF&09f8ff "
   a.分别统计出word中英文字母(isalpha)、空格(isspace)、数字(isdigit)和其它字符的个数。
   b.将word中的小写字母全部转换成大写字母(upper)，输出到控制台。
   c.将word中的小写字母和大写互换(比如Hello-->hELLO)(swapcase)，输出到控制台。
   d.请将word字符串的数字取出，并输出成一个新的字符串(+)。
"""
word = "ghSk 45s Df,9 87.fs sF&09f8ff "

num_cap = 0
num_small = 0
num_digit = 0
num_space = 0
num_other = 0

len_string = len(word)
i = 0
str01 = "abcdefghijklmnopqrstuvwxyz"
str02 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str03 = "0123456789"
str04 = " "
while i < len_string:
    if word[i] in str01:
        num_small += 1
    elif word[i] in str02:
        num_cap += 1
    elif word[i] in str03:
        num_digit += 1
    elif word[i] in str04:
        num_space += 1
    else:
        num_other += 1
    i += 1

print("您输入的字符串中包含%d个大写字母，%d个小写字母，%d个数字，%d个空格，%d个其他字符" % (num_cap, num_small, num_digit, num_space, num_other))


num_alpha = 0
num_digit = 0
num_space = 0
num_other = 0
for w in word:
    if w.isalpha():
        num_alpha += 1
    elif w.isdigit():
        num_digit += 1
    elif w.isspace():
        num_space += 1
    else:
        num_other += 1
print("您输入的字符串中包含%d个字母,%d个数字，%d个空格，%d个其他字符" % (num_alpha, num_digit, num_space, num_other))

