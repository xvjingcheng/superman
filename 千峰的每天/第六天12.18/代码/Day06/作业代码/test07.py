"""
7、模拟银行账户业务，实现存款、取款和余额查询。运行效果如下所示：

1.存款  2.取款  3.查询  0.退出
请选择你要办理的业务：1
请输入存款金额：1000
---------
存款成功！

1.存款  2.取款  3.查询  0.退出
请选择你要办理的业务：2
请输入取款金额：100
---------
取款成功！

1.存款  2.取款  3.查询  0.退出
请选择你要办理的业务：
---您当前账户余额：900元---

1.存款  2.取款  3.查询  0.退出
请选择你要办理的业务：0
<!--  -->
O(∩_∩)O谢谢您的使用，欢迎下次光临！
"""
# 总额
import time

total_money = 0


# 存款的函数
def save_money(total_money):
    while True:
        money = input("请输入存款金额:")
        # 判断存入金额的合法性
        if money.isdigit():
            money = int(money)
            # 判断存入的是否是整钞
            if money % 100 == 0:
                total_money += money
                print("存入成功，当前余额%d元" % total_money)
                break
            else:
                print("请存入整钞")
        else:
            print("请输入合法金额:")
    return total_money


# 取款的函数
def take_money(total_money):
    while True:
        # 提示用户输入数据
        money = input("请输入取款金额:")
        if money.isdigit():
            money = int(money)
            # 判断是否是整钞
            if money % 100 == 0:
                # 判断余额是否充足
                if total_money >= money:
                    total_money -= money
                    print("取款成功，当前余额%d元" % total_money)
                else:
                    print("余额不足")
                break
            else:
                print("请输入100的倍数")
        else:
            print("请输入合法金额")
    return total_money


while True:
    # 提示用户输入数据
    print("1.存款  2.取款  3.查询  0.退出")
    select = input("请选择你要办理的业务：")
    # 判断用户输入内容的合法性
    if select.isdigit():
        select = int(select)
        # 根据用户选择，执行不同操作
        if select == 0:
            print("O(∩_∩)O谢谢您的使用，欢迎下次光临！")
            break

        elif select == 1:
            # 存款
            total_money = save_money(total_money)
        elif select == 2:
            # 取款
            total_money = take_money(total_money)
        elif select == 3:
            print("正在查询余额...")
            time.sleep(3)
            print("查询成功,当前余额%d元" % total_money)
        else:
            print("您的输入有误，请重新输入")
    else:
        print("您的输入有误，请重新输入")

print("操作结束，当前余额%d元" % total_money)
