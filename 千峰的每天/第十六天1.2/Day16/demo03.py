def add_num(a, b):
    return a + b


def sub_num(a, b):
    return a - b


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        print("开始测试时候调用")

    def tearDown(self):
        print("测试结束时候调用")

    def test_add(self):
        self.assertEqual(add_num(1, 2), 4, "加法不行")

    def test_sub(self):
        self.assertEqual(sub_num(5, 2), 2, "减法不行")


if __name__ == '__main__':
    unittest
