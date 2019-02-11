"""
核心代码
"""
import time


def 核心代码():
    # 开始时间
    start_time = time.time()

    print("hello")
    time.sleep(1)
    print("world")

    # 结束时间
    end_time = time.time()

    # 消耗时间
    total_time = end_time - start_time

    print("消耗总时间%s" % total_time)


核心代码()
