"""
type创建带有__init__()的类

"""


def __init__(self):
    self.r = "rrr"
    self.s = "sss"


def show14(self):
    print("show14")

Demo12 = type("Demo12", (object,), {})
