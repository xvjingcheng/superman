"""
 5、将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
"""
num = int(input("请输入一个正整数:"))
print(num, end="=")
for i in range(1, num + 1):
    for index in range(2, num + 1):
        if num % index == 0:
            num = int(num / index)
            if num == 1:
                print(index)
            else:
                print(index, end="*")
            break
