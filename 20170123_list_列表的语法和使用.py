#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 创建一个列表,可包含字符串，数字，布尔值，列表，列表中还可嵌套列表
team =  ["alex","True",78,100,2,"jenny","prince",[6,"mark",-9],"zhangsan","lisi",100,-111,"ada","bruce",333,"cathy",111,"daisy","eric"]

# 打印列表
print(team)

# 遍历列表中的所有元素
for i in team:
    print(i)

# 查看列表中的元素个数
print(len(team))

# 使用下标调取列表元素："jenny"
print(team[5])
# 调取最后一个元素："eric"
print(team[-1])
# 调取倒数第四个元素："cathy"
print(team[-4])
# 调取第5至第7连续的三个元素：2,"jenny","prince"
print(team[4:7])
# 调取倒数第2至倒数第5连续的四个元素：333,"cathy",111,"daisy"
print(team[-5:-1])
# 从第12至第18每隔2个元素调取一个：-111, 'bruce', 'cathy', 'daisy'
print(team[11:18:2])  # 开始元素下标:结束元素下标:跳数
# 从头至尾每隔5个元素调取一次：'alex', 'jenny', 100, 'cathy'
print(team[::5])  # 第1个元素和最后一个元素可省略不写,仅写跳数
# 调取嵌套列表中的元素"mark"
print(team[7][1])

# 修改指定下标所在的元素
team[1] = False  # 将 True 修改为 False
team[7][0] = -6  # 将嵌套列表中的6 修改为 -6
print(team)

# 追加新元素"gates"到列表末尾,每次只能追加一个
team.append("gates")
print(team)

# 追加一个列表作为元素到列表末尾
dev = ["miki","lori","Maria"]
team.append(dev)
print(team)

# 插入新元素“jobs”到第10位
team.insert(9,"jobs")
print(team)

# 追加指定列表中的元素到列表中
ope = ["rick","grace"]
team.extend(ope) # 将ope中的两个元素"rick","grace"追加到team中
print(team)

# 统计指定元素在列表中重复的次数
print(team.count(100)) # 列表中100重复的次数是2

# 统计指定元素在列表中最低位索引
print(team.index(100)) # "100"的最小下标是3

# 将列表中所有的100全部修改为200
for i in range(team.count(100)):
    ele_index = team.index(100)
    team[ele_index] = 200
print(team)

# 删除列表最后一个元素
team.pop()
print(team)

# 删除列表中指定下标的元素
team.pop(8)
print(team)

# 删除列表中的"ada"
team.remove("ada")
print(team)

# 将列表中的元素排序
# print(team.sort())  # python3不能对不同数据类型进行排序，但python2支持

# 反转列表中的元素，即前后颠倒元素的排序
team.reverse() # 此方法不返回任何值
print(team)

# 清空列表中所有的元素
team.clear()
print(team)


# copy()与deep_copy()的区别
import copy

list = ["one",2,["three",4],5]
copy0 = list.copy()  # python3不能list.deepcopy(),why？
copy1 = copy.copy(list)
copy2 = copy.deepcopy(list)

print("list:",list)
print("copy0:",copy0)
print("copy1:",copy1)
print("copy2:",copy2)
print(list == copy0) # True
print(list is copy0) # False
print(copy1 == copy2)  # True
print(copy1 is copy2)  # False
print(id(list),id(copy0),id(copy1),id(copy2)) # 四个id各不相同

# !!! 进行以下任一种情况测试时，请注释掉剩余三种情况的代码 !!!

#当list的元素发生变化时
'''
list[3] = "five"
list[2][0] = 3
print("list:",list)   # list: ['one', 2, [3, 4], 'five']
print("copy0:",copy0) # copy0: ['one', 2, [3, 4], 5]
print("copy1:",copy1) # copy1: ['one', 2, [3, 4], 5]
print("copy2:",copy2) # copy2: ['one', 2, ['three', 4], 5]
'''

#当copy0的元素发生变化时
'''
copy0[3] = "five"
copy0[2][0] = 3
print("list:",list)   # list: ['one', 2, [3, 4], 5]
print("copy0:",copy0) # copy0: ['one', 2, [3, 4], 'five']
print("copy1:",copy1) # copy1: ['one', 2, [3, 4], 5]
print("copy2:",copy2) # copy2: ['one', 2, ['three', 4], 5]
'''

# 当copy1的元素发生变化时
'''
copy1[3] = "five"
copy1[2][0] = 3
print("list:",list)   # list: ['one', 2, [3, 4], 5]
print("copy0:",copy0) # copy0: ['one', 2, [3, 4], 5]
print("copy1:",copy1) # copy1: ['one', 2, [3, 4], 'five']
print("copy2:",copy2) # copy2: ['one', 2, ['three', 4], 5]
'''

# 当copy2的元素发生变化时
'''
copy2[3] = "five"
copy2[2][0] = 3
print("list:",list)   # list: ['one', 2, ['three', 4], 5]
print("copy0:",copy0) # copy0: ['one', 2, ['three', 4], 5]
print("copy1:",copy1) # copy1: ['one', 2, ['three', 4], 5]
print("copy2:",copy2) # copy2: ['one', 2, [3, 4], 'five']
'''

# 结论
# 1. 修改原始列表中非嵌套列表的元素,不会影响copy()和deepcopy()
# 2. copy()不会完整复制原始列表中的嵌套列表作为独立存在，而只是将嵌套类表原数据打上新标签，当嵌套列表原数据改变，copy()也会随之改变
# 3. deepcopy()会连带嵌套列表一起完整复制作为独立存在，修改嵌套列表中的元素，既不会影响原始列表，也不会被原始列表影响
