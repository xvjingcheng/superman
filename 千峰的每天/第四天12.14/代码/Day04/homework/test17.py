"""
17.猴子吃桃问题：
猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个
第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上都吃了前一天剩下的一半零一个。
到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少
day10   1
day09   (1+1) * 2
day08   (4+1) * 2
day07   (10+1) * 2
"""
result = 1
for i in range(9):
    result = (result + 1) * 2
else:
    print("猴子第一天摘下%d颗桃子" % result)
