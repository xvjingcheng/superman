"""
递归
    函数内部调用自己
"""


def show():
    print("放飞自我")
    show()


# show()

"""
5! = 5 * 4 * 3 * 2 * 1
   = 5 * 4!
   = 5 * 4 * 3!
   = 5 * 4 * 3 * 2!
   = 5 * 4 * 3 * 2 * 1!
   = 5 * 4 * 3 * 2
   = 5 * 4 * 6
   = 5 * 24
   = 120
   
    f(n) * f(n-1)!

"""

# result = 1
# # num = 5
# # while num > 0:
# #     result *= num
# #     num -= 1
# #
# # print(result)


def get_mul(num):
    if num >= 1:
        result = num * get_mul(num - 1)
        print(id(result))
    else:
        result = 1
        print(id(result))
    return result


print(get_mul(5))
"""
num = 5
    result = 5 * get_mul(4)
         = 5 * 4 * get_mul(3)
             = 5 * 4 * 3 * get_mul(2)
                 = 5 * 4 * 3 * 2 * get_mul(1)
                     = 5 * 4 * 3 * 2 * 1 * get_mul(0)
                        get_mul(0) = 1

"""

print(get_mul(996))
