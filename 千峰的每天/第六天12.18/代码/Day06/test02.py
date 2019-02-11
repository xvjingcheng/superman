"""
2、制作4位字符组成随机验证码，4位字符组成，不区分大小写
	流程：
	- 用户执行程序
	- 给用户显示需要输入的验证码
	- 用户输入的值
		用户输入的值和显示的值相同时实现正确信息;
		否则继续生成随机验证码继续等待用户输入
	生成随机验证码代码示例：
	# (print(chr(97))：输出结果为a)
"""
import random

while True:
    str00 = ""
    for i in range(4):
        char1 = random.choice([chr(random.randint(65, 90)), chr(random.randint(97, 122))])
        str00 += char1
    print(str00)
    str01 = input("请输入验证码:")
    if str00.upper() == str01.upper():
        print("验证成功")
        break
    else:
        print("验证码错误，请重新输入")


