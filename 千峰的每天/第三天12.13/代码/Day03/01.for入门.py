"""
# 跟媳妇表白，说一万遍“我想你”
print("我想你。。。。")
print("我想你。。。。")
print("我想你。。。。")
print("我想你。。。。")
"""
import time

for i in range(10, 0, -1):
    print("我第%d次想你。。。。" % i)
    # time.sleep(1)

sum = 0
for i in range(0, 101, 2):
    sum += i
print(sum)

sum = 1
for i in range(2, 101, 2):
    sum *= i
print(sum)

names = ["白炳钿", "许京城", "龚诗清", "黎莹", "王新鑫", "施惠玲", "李志钰", "刘鑫", "王合成", "陈丽威", "蔡胜", "董玉烽",
         "翁继星", "陈道表", "姚佳雯", "王品力", "姚蓄", "毛晗", "严心雨", "张飒", "胡宗泉", "张涛", "陈相钻"]

print(len(names))
