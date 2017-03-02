#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:MingguiLu
# title:set集合

print("定义set集合")
s1 = {1,2,3,4,5,10}
print(s1)

s2 = {10,11,12,13,14,15}
print(s2)

s3 = set()
s4 = set([100,200,300,400,500])
print(s3)
print(s4)

# .add 添加元素至集合，每次一个，如果元素已存在不起作用
print("\n调用.add添加元素")
s1.add(6)
print(s1)

s2.add(16)
print(s2)

s3.add(10)
s3.add(20)
print(s3)

s4.add(600)
print(s4)

# .copy 浅拷贝一个集合
print("\n调用.copy浅拷贝")
s5 = s3.copy()
s3.add(30)
print(s3)
print(s5)   # 由于s5是浅拷贝自s3,当s3元素发生改变不影响s5


# .difference 比较两个或多个集合的差异元素并返回一个新集合
print("\n调用.difference比较差异元素")
dif1 = s1.difference(s2)
print(dif1)                 # 结果为：{1, 2, 3, 4, 5, 6}，即s1中有但s2中没有的元素
dif2 = s2.difference(s1)
print(dif2)                 # 结果为：{11, 12, 13, 14, 15, 16}，即s2中有但s1中没有的元素
dif3 = s3.difference(s4)
print(dif3)                 # 结果为：{10, 20, 30}，即s3中有但s4中没有的元素

# .difference_update 比较两个或多个集合,将共有的元素从原集合移除，仅保留不同的元素
print("\n调用.difference_update移除共有元素")
s6 = {'a','b','c','d','e'}
s7 = {'c','d','e','f','g'}
s8 = {'e','f','g','h','i'}
s7.difference_update(s6,s8)
print(s7)                   # 结果为：set()，s7与s6、s8共有的元素c、d、e、f、g从s7中全部移除，变为空集合

# .discard 从集合中移除一个存在的元素,如果集合中不存在该元素，则不起作用
print("\n调用.discard移除存在的元素")
s9 = {'tom','jenny','joy','jade'}
s9.discard("nate")
print(s9)                   # 结果为：{'tom', 'jade', 'jenny', 'joy'}，s9中不存在nate元素，所以未对集合产生影响
s9.discard("joy")
print(s9)                   # 结果为：{'tom', 'jade', 'jenny'}，从s9中将joy移除了

# .intersection 返回两个集合中公共的元素作为一个新集合
print("\n调用.intersection返回包含共有元素的新集合")
s10 = {'jenny','jade','Ella','tony'}
print(s9.intersection(s10))

# .intersection_update　将集合的元素更新为两个集合元素的交集
print("\n调用.intersection_update")
print(s9)
print(s10)
s9.intersection_update(s10)
print(s9)                    # 结果为：{'jenny', 'jade'}，s9的元素更新为s9和s10的交集jenny、jade

# .isdisjoint 如果两个集合元素没有交集，返回true,否则返回false
print("\n调用.isdisjoint判断两个集合是否没有交集")
s11 = {'a','b','c'}
s12 = {'c','d','e'}
s13 = {'e','f','g'}
print(s11.isdisjoint(s12))  # 结果为：　False，s11和s12元素存在交集c
print(s12.isdisjoint(s13))  # 结果为：　False，s12和s13元素存在交集e
print(s13.isdisjoint(s11))  # 结果为：　True，s13和s11元素没有交集

















