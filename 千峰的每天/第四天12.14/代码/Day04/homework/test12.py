"""
12.A、B、C、D分别为0~9之间的整数，求出满足AB+CD=DA条件的数。
例如：90+09=99
"""
for A in range(10):
    for B in range(10):
        for C in range(10):
            for D in range(10):
                if (10 * A + B) + (10 * C + D) == (10 * D + A):
                    print("A=%d,B=%d,C=%d,D=%d" % (A, B, C, D))
