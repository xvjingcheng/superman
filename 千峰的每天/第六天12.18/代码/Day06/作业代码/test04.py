"""
4、声明一个方法，录入3个数字，返回其中的最大值
"""


def get_max():
    num01 = int(input("请输入第一个数字:"))
    num02 = int(input("请输入第二个数字:"))
    num03 = int(input("请输入第三个数字:"))
    # 使用max方法比较三个值，返回最大的那个
    num_max = max(num01, num02, num03)
    return num_max


num_max = get_max()
print("您输入的最大的值是%d" % num_max)
