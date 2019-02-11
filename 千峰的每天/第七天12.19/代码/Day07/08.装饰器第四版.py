"""
核心代码
"""
import time


def 核心代码():
    print("hello")
    time.sleep(1)
    print("world")


def 测试代码(fun):
    def 包装器():
        # 开始时间
        start_time = time.time()

        # 核心代码
        fun()

        # 结束时间
        end_time = time.time()
        # 消耗时间
        total_time = end_time - start_time
        print("消耗总时间%s" % total_time)

    return 包装器


包装器 = 测试代码(核心代码)
print(包装器)

包装器()
