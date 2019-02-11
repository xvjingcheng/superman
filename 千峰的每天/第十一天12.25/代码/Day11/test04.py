"""
4. 创建银行类，模拟登录、存、取、查询、转账、退出功能，对敏感的数据进行保护
需求说明
登录银行首先输入账号和密码，一共三次机会
登陆后开启
存(saveMoney)、取(drawMoney)、查询(checkMoney)、转账(Transfer accounts)、退出(quit)功能
"""


class ABCBand(object):

    def __init__(self):
        self.total = 0
        self.isLogin = False
        self.username = "dujunqiang"
        self.password = "111222"

    def login(self, username, password):
        if (self.username == username) and (self.password == password):
            self.isLogin = True

        return self.isLogin

    def save(self, money):
        if self.isLogin:
            if money > 0:
                self.total += money
            else:
                print("输入金额有误")
        else:
            print("请先去登录")
        return self.total

    def take(self, money):
        if self.isLogin:
            if self.total >= money:
                self.total -= money
            else:
                print("余额不足")
        else:
            print("请先去登录")
        return self.total

    def __str__(self):
        if self.isLogin:
            return "您的账户余额为:%d元" % self.total
        else:
            return "请先去登录"


LaoLi = ABCBand()
count = 0
while True:
    username = input("请输入用户名:")
    password = input("请输入密码:")
    if LaoLi.login(username, password):
        print("登录成功")
        LaoLi.save(10000000000000)
        print(LaoLi)
        LaoLi.take(2)
        break
    else:
        print("登录失败，请重新输入")
    count += 1

    if count == 3:
        break

print(LaoLi)
