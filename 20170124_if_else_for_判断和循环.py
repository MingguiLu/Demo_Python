#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:IMKind


'''
1. 本例说明：
    模拟系统登录。允许用户登录验证5次，登录成功进入系统，登录失败会提示用户剩余次数。
2. 本例实践if条件判断和for循环
'''

import getpass  # 调用标准库的getpass模块，用户输入是隐藏回显

user = "root"
passwd = "password@123"

for i in range(5):
    username = input("username:")
    password = getpass.getpass("password:") # !!!注意: IDE可能不支持隐藏回显，如果在IDE中报错了，请在终端中测试
    if user == username and passwd == password:
        print("欢迎登录！")
        break
    else:
        if i == 4:
            print("错误次数已达到5次，请稍后再试！")
        else:
            print("用户名或密码错误,您还有%s次机会！" %(4-i))







