"""
list_produce = [['Iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]
dict00 = {}
list00 = []
num00 = str(input("请输入商品编号:"))
while str(num00) != "q":
    if int(num00) <= 5:
        dict00[list_produce[int(num00)][0]] = list_produce[int(num00)[1]]
        list00.append(list_produce[int(num00)])
        num00 = str(input("请输入商品编号:"))
    else:
        print("商品编号输入有误，请重新输入")
        num00 = str(input("请输入商品编号:"))
print("用户选择商品有:", end="")
for key in dict00:
    print(key, end="\t")
sum00 = 0
for i in range(len(list00)):
    sum00 += list00[i][1]
print("总价格为%d" % sum00)
"""

list_produce = [['Iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]
list_cart = []

while True:
    for produce in enumerate(list_produce):
        print(produce)
    select = input("请输入商品编号:")
    if select.isdigit():
        select = int(select)
        if select < 6:
            list_cart.append(list_produce[select])
    elif select == "q":
        sum_price = 0
        for price in list_cart:
            sum_price += price[1]
        break
    else:
        print("您的输入有误，请检查后重新输入")

print(list_cart)
print(sum_price)
