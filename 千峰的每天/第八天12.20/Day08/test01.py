"""
不定长参数
"""


def demo00(a, b=12000, *args, **kwargs):
    result = a + b
    print(a)
    print(b)
    print(args)
    print(kwargs)
    return result


demo00(3, 5)
demo00(b=5, a=3)
args = (100, 600, 200)
kwargs = {"name": "Lucy"}
demo00(6000, 12000, args, kwargs)
