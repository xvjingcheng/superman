from functools import reduce

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
print(reduce(lambda x, y: x - y, [1, 2, 3, 4, 5]))
print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))

print(reduce(lambda x, y: x + y, ["1", "2", "3", "4", "5"]))

print(reduce(lambda x, y: x + y, range(101)))


def get_result(a, b):
    return a + b


print(reduce(get_result, [6, 7, 8, 9, 10]))
# print(reduce(get_result, 12345))
