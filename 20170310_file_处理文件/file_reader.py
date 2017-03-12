#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:MingguiLu

'''读取整个文件内容'''
print("\n读取整个文件内容:")

with open('pi_digits.txt') as file_object:
    '''打开文件'''
    print(file_object.read())
    '''打印文件内容'''

with open('pi_digits.txt') as file_object:
    '''打开文件'''
    pi = file_object.read()
    '''读取文件内容并赋给变量pi'''
    print(pi.replace("\n","").replace(" ",""))
    '''使用.replace()将每行末尾的换行符和空格，替换为空，打印格式化好的π'''


'''使用相对路径读取文件'''

with open('text_files/relative_path.txt') as file_object:
    '''使用相对路径打开目录中的文件'''
    pi = file_object.read().rstrip()
    print(pi)


'''使用绝对路径读取文件'''

file_name = '/home/imkind/helloworld/pycharmProjects/learnPython/20170310_file_处理文件/text_files/absolute_path.txt'
'''将文件绝对路径赋给变量file_name'''

with open(file_name) as file_object:
    '''使用绝对路径打开目录中的文件'''
    pi = file_object.read()
    '''读取文件内容病赋给变量pi'''
    print(pi)
    '''打印文件内容'''


'''逐行读取'''
print("\n逐行读取:")

file_name = 'pi_digits.txt'
'''将文件名称赋给变量'''

with open(file_name) as file_object:
    '''打开文件'''
    for line in file_object:
        '''逐行读取文件内容'''
        print(line)
        '''逐行打印文件内容，
        结果每隔一行都打印一个空行，
        这是因为文件的每行末尾都有一个换行符，而print语句也会加上一个换行符，
        造成打印结果每行末尾有两个换行符，即空行.可使用rstrip()消除多余的空白行'''


'''逐行读取内容并拼接字符串'''
print("\n逐行读取内容并拼接字符串：")

with open('pi_digits.txt') as file_object:
    '''打开文件'''
    pi = ''
    '''初始化变量pi'''
    for line in file_object:
        '''逐行读取文件的每一行内容'''
        pi += line.strip()
        '''剔除元素首尾的空字符后做字符串拼接，并赋给pi'''
        # pi += "".join(line.strip())
    print(pi)
    '''打印拼接完成的π'''


'''readline()每次读取一行内容'''

print("\nreadline()每次读取一行内容并拼接为字符串：")

with open('pi_digits.txt') as file_object:
    '''打开文件'''
    pi = ''
    '''初始化变量pi'''
    while True:
        '''???'''
        line = file_object.readline()
        '''读取一行内容赋给变量line'''
        if line:
            '''如果读取到一行数据'''
            #print(line)
            pi += line.strip()
            '''剔除这行数据两端的空字符之后拼接并赋给pi'''
        else:
            '''如果读取内容为空'''
            break
            '''退出循环'''
    print(pi)


'''创建一个包含文件各行内容的列表'''
print("\n创建一个包含文件各行内容的列表:")


'''方法一'''
print("\n方法一：.readlines()")

with open('pi_digits.txt') as file_object:
    '''打开文件'''
    lines = file_object.readlines()
    '''读取文件的每行作为元素存入列表'''
    print(lines)
    '''打印列表'''
    pi = ''
    '''初始化变量pi'''
    for line in lines:
        '''遍历列表的元素'''
        pi += line.strip()
        '''剔除元素首尾的空字符后做字符串拼接，并赋给pi'''
    print(pi)
    '''打印拼接完成的字符串'''

'''方法二'''
print("\n方法二：.split()")

with open('pi_digits.txt') as file_object:
    '''打开文件'''
    lines = file_object.read().split()
    '''将文件分割为字符串列表'''
    print(lines)
    '''打印列表'''
    pi = ''
    '''初始化变量pi，用于表示完整的π'''
    for line in lines:
        '''遍历列表的元素'''
        pi += line
        '''将每个元素做字符串拼接，并赋给pi'''
    print(pi)
    '''打印拼接完成的字符串,获得π'''





