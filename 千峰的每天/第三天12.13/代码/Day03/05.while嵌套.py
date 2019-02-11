"""
*******
*******
*******
*******
*******
"""
import math

i = 1
while i <= 5:
    j = 1
    while j <= 7:
        print("*", end="")
        j += 1
    print()
    i += 1

"""
*
* *
* * *
* * * *
* * * * *
"""

i = 1
while i <= 5:

    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

i = 1
while i <= 9:

    if i <= 5:
        j = 1
        while j <= i:
            print("*", end=" ")
            j += 1
    else:
        j = 1
        while j <= (10 - i):
            print("*", end=" ")
            j += 1

    print()

    i += 1

print("*" * 30)
i = 1
while i <= 9:

    j = 1
    while j < math.fabs(5-i):
        print("*", end=" ")
        j += 1
    print()

    i += 1
