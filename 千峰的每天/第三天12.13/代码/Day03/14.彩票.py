"""
实现双色球的彩票功能。
规则：从33个红球中随机选择不重复的6个数，从15个篮球中随机选择1个组成一注彩票，可以选择买多注。
"""
import random

colorful_ticket = []

for i in range(1, 1000):
    num = random.randint(1, 33)
    if num not in colorful_ticket:
        colorful_ticket.append(num)
    if len(colorful_ticket) == 6:
        colorful_ticket.sort()
        break
colorful_ticket.append([random.randint(1, 16)])
print(colorful_ticket)

print(sorted(random.sample(range(1, 34), 6)))

