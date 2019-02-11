def add2num(a, b):
    result = a + b
    return result


print(add2num(3, 5))

import math


def get_area(a, b, c):
    p = get_Perimeter(a, b, c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area


def get_Perimeter(a, b, c):
    p = a + b + c
    return p


area = get_area(3, 4, 5)
print(area)
