"""
*
*  *
*  *  *
*  *  *  *
*  *  *  *  *
"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="\t")
    print()

b = 0
c = 1
for i in range(10):
    # b, c = c, b + c
    # 引入第三个变量交换变量的值
    temp = c
    c = b + c
    b = temp
    print(b)

# 老王买鸡
# 今有鸡翁一，值钱伍；母鸡一，值钱三；鸡鶵三，值钱一。凡百钱买鸡百只，问鸡翁、母、鶵各几何？
for gong in range(1, 20):
    for mu in range(1, 33):
        for chu in range(3, 99, 3):
            if (gong + mu + chu) == 100 and (gong * 5 + mu * 3 + chu / 3) == 100:
                print("公鸡%d只，母鸡%d只，雏鸡%d只" % (gong, mu, chu))


