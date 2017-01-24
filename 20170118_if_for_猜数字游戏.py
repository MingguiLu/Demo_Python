#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
1. 本例说明：
    猜数字游戏。可根据每次输入数字后的提示，猜测指定的数字。当猜测5次后程序会询问是否继续，继续则再猜5次，不继续则程序结束，共10次机会！
2. 本例实践if条件判断和for循环
3. 本例实践break跳出循环和continue跳过循环
'''
age = 66
num = 0
for i in range(11):
    # print("num is :",num)
    if num < 5 :
        guess_age = int(input("Please enter your guess age:"))
        if age == guess_age:
            print("Congratulations! You got it! You take",i+1,"times!")
            break
        elif age > guess_age:
            print("Your enter is small !")
        else:
            print("Your enter is big !")
    else:
        continue_confirm =  input("Do you want to continue?(y/n):")
        if continue_confirm == "y" :

            num = 0
            continue
        else:
            print("Byebye!")
            break
    num += 1