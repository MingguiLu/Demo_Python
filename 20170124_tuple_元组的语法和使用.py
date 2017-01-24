#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:IMKind

# 创建一个元组(tuple)
hubei = ("wuhan","yichang","xiangyang","shiyan","enshi","xianning","huangshi")

# 打印tuple
print(hubei)

# 遍历tuple中的所有元素
for i in hubei:
    print(i)

# tuple一旦初始化就不能修改,没有append()，insert()这样的方法,也不能重新赋值成另外的元素
# hubei[-1] = "hankou"    # 该语句执行回报错:TypeError: 'tuple' object does not support item assignment

# 查看tuple中的元素个数
print(len(hubei))

# 统计指定元素在tuple中重复的次数
print(hubei.count("wuhan"))

# !!!当创建仅包含一个数字元素的tuple时，元素后面要加一个`,`来消除歧义，否则`()`被表示为数学公式中的小括号
num = (1)
print(num)               # 结果是数字 1

num = (1,)
print(num)               # 结果是 (1,)

# !!!tuple的元素可以是多层嵌套list
num = (1,2,["three","four",[5,6]],7)
print(num)               # (1, 2, ['three', 'four', [5, 6]], 7)

# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。但指向的嵌套list本身是可变的！
num[2][0] = 3
num[2][2][0] = "five"
print(num)               # (1, 2, [3, 'four', ['five', 6]], 7)

# 要创建一个完全不能改变的tuple,每个元素本身也必须不能改变
num = (1,2,("three","four",(5,6)),7)
# num[2][0] = 3          # TypeError: 'tuple' object does not support item assignment
# num[2][2][0] = "five"    # TypeError: 'tuple' object does not support item assignment
print(num)               # (1, 2, ('three', 'four', (5, 6)), 7)











