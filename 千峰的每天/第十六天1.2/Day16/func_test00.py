import doctest
"""
文档测试
    测试代码在文档中
    需要导入doctest
    注释文档中使用 >>> 测试内容
    使用doctest.testmod()调用
    
"""


def get_result(a, b, c):
    """

    :param a:
    :param b:
    :param c:
    :return:

    >>> print(get_result(2,3,5))
    11
    """
    result = a + b + c
    return result


doctest.testmod()
