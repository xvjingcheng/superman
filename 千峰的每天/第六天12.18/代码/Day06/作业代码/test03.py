"""
3、声明一个函数，根据输入的两个数输出这两个数字的乘积
    函数定义方式
        def 函数名(参数1，参数2):   形参
            方法体
            sum00 = 参数1 * 参数2
            return sum00
    调用函数
        函数名(参数1，参数2)    --》 有的时候可以没有参数
"""
import keyword

print("def" in keyword.kwlist)


# 定义函数，函数有两个参数，在这里的参数叫做形参
def mul00(a, b):
    product = a * b
    print(product)


"""
参数
    参与运算的变量
形参
    形式上的参数--》形式上的变量
实参
    实际参与运算的变量/常量--》替换方法参数列表中的形参
"""
x = 3
y = 5
# 调用函数mul，括号里面的是实参，会替换掉函数中的形参参与运算
mul00(x, y)

"""
# 通知的作用
def notice():
    print("亲爱的旅客朋友们，你们旅途辛苦啦，特产店又好吃的，赶快去吧")


notice()

"""
"""
送水
    买水的钱
    送水师傅送水的方法
    水送过来
"""

list00 = [1, 4, 7, 4, 2, 8, 0]
list00.sort()

list01 = sorted(list00)


def mul01(a, b):
    produce = a * b
    return produce


result = mul01(3, 5)
print("得到的结果的2倍是%d" % (result*2))
