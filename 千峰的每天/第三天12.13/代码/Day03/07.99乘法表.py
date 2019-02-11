"""
1 * 1 = 1
1 * 2 = 2   2 * 2 = 4
1 * 3 = 3   2 * 3 = 6   3 * 3 = 9
... ...
"""

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print("%d * %d = %d" % (j, i, j*i), end="\t")
#         j += 1
#
#     print()
#
#     i += 1

# while True:
#     print("fghjkl;lkgjklkj")

# DDOS攻击

for i in range(1,10):
    for j in range(1,i+1):
        print("%d * %d = %d" %(j,i,i*j),end="\t")
    print()