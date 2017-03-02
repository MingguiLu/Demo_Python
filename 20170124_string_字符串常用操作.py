#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:IMKind

# 定义一个字符串
str1 = "python is a programming language that lets you work quickly and integrate systems more effectively."

# 统计指定字符的重复次数
print(str1.count("m"))  # 4

# 统计指定字符的最低位索引
print(str1.index("m"))  # 18

# 首字符转换为大写
print(str1.capitalize())    # Python is a ...

# 转换所有大写字符为小写，与lower()类似，区别在于lower()只对ASCII码(A-Z)有效,casefold()对其他语言也有效
str2 = "ß"  # 德语中的"ß"，对应的小写是"ss"
print(str2.casefold())  # ss

#
print(str1.center(20,"-"))