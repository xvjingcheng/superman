import logging

# 设置显示日志等级
logging.basicConfig(level=logging.INFO)


def get_result(a, b):
    logging.info("a=%d,b=%d" % (a, b))
    c = a + b
    return c


print(get_result(3, 5))

print("*" * 20)

logging.basicConfig(level=logging.ERROR)


def get_result(a, b):
    logging.error("a=%d,b=%d" % (a, b))
    c = a + b
    return c


print(get_result(3, 5))
