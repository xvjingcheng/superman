"""
5、编写代码，实现双色球彩票一键选号功能：
		红球6个，号码在1—33之间，按从小到大排列
		篮球一个，排列在红球后面
		以字典的形式输出到控制台
		例如:{"红球":[1,2,3,4,5,6],"蓝球":[1]}
"""
import random

red_ball = random.sample(range(1, 34), 6)
blue_ball = random.randint(1, 16)
dict00 = {"红球": sorted(red_ball), "蓝球": blue_ball}
print(dict00)
