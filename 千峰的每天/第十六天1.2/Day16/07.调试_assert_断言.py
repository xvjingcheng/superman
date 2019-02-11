"""
assert 断言

"""


def get_result(a, b):
    assert b != 0, "被除数不能为0"
    c = a / b
    return c


print(get_result(10, 1))


def get_sum(a):
    assert isinstance(a, int), "运算的参数必须是数字"
    result = a ** 2
    return result


num = input("请输入一个整数:")
num = int(num)
print(get_sum(num))
