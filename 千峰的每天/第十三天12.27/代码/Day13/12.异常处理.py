"""
try:
    可能报错的代码
    ...
except Exception as e:
    出错之后的操作
    ...
else:
    不出错会执行
finally:
    不论报错与否都会执行
"""
import os

print("核心代码")

try:
    os.rename("file", "file00")
    # print("lalala")
    print("hello"[0])
except Exception as e:
    print(e)
else:
    print("没有报错")
finally:
    print("关闭电源，放掉那个人")

print("比核心代码还重要的代码")
