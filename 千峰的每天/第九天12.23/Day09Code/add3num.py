def get_result(*args):
    """
    计算任意个数数字的和
    :param args:
    :return:
    """
    result = 0
    for a in args:
        result += a
    print(__name__)
    return result


# 测试用的代码，只能在本模块中运行时会执行if中的内容，如果是其他模块调用本模块，if条件不成立
if __name__ == "__main__":
    print(get_result(1, 2, 3, 5, 4))
    print(__name__)

# www.1000phone.com
