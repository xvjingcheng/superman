"""
不定长参数之**kwargs
    传入参数时，先满足args的数量，剩余的正常格式的参数给*args，关键字参数给**kwargs

    定义不定长参数时，需要把args放在前面，*args方第二位，**kwargs放在最后
"""


def show(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)
    for key, value in kwargs.items():
        print(key, ":", value)


show("张三", 18, 13801234567, "ZHANGSAN@163.com", address="九堡")
# show(22, "male", "ddddd@126.com", name="李斯")

"""
姓名
** 性别
** 年龄
* 民族
* 政治面貌
** 学历
** 毕业院校
** 手机号码
** 邮箱
"""
