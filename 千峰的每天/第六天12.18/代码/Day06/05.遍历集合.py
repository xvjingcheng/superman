"""
遍历集合
    集合没有下标，无法通过下标访问某个元素，所以无法使用while遍历
    可以使用for遍历集合
"""
set00 = set("你的对手在学习，你的敌人在磨刀。你的闺蜜在减肥，隔壁老王在练腰。")

for w in set00:
    print(w, end="\t")

for w in enumerate(set00):
    print(w)
