#!/usr/bin/env python3
# -*- coding: utf-8 -*-


name = input("Please input your name:")
age = int(input("Please input your age:")) #convert str to int
job = input("Please input your job:")
salary = float(input("Please input your salary:")) #convert str to float

msg = '''
%s 的个人信息如下:
----------------------
姓名： %s
年龄： %d
工作： %s
薪水： %f
---------END----------
''' % (name,name,age,job,salary)

print(msg)

