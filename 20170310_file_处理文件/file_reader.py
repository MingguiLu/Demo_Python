#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:MingguiLu

'''读取整个文件内容'''

with open('pi_digits.txt') as file_object:
    '''打开文件'''
    print(file_object.read())
    '''打印文件内容'''

with open('pi_digits.txt') as f_obj:
    '''打开文件'''
    content = f_obj.read()
    '''读取文件内容并赋给变量content'''
    print(content.rstrip())
    '''.read()到达文件末尾时返回一个空字符串，显示出来就是一个空行，可使用rstrip()删除末尾的空白'''


'''使用相对路径读取文件'''

with open('text_files/relative_path.txt') as file_object:
    '''使用相对路径打开目录中的文件'''
    print(file_object.read().rstrip())


'''使用绝对路径读取文件'''

file_name = '/home/imkind/helloworld/pycharmProjects/learnPython/20170310_file_处理文件/text_files/absolute_path.txt'
'''将文件绝对路径赋给变量file_name'''

with open(file_name) as file_object:
    '''使用绝对路径打开目录中的文件'''
    content = file_object.read()
    '''读取文件内容病赋给变量content'''
    print(content)
    '''打印文件内容'''


'''逐行读取'''

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



'''创建一个包含文件各行内容的列表'''

'''方法一'''

file_name = 'pi_digits.txt'
'''将文件名称存储在变量file_name'''

with open(file_name) as file_object:
    '''打开文件'''
    lines = file_object.read().split()
    '''读取文件每行内容作为元素存入列表'''
    print(lines)
    '''打印列表'''

    content = ''
    '''初始化变量content，用于表示完整的π'''
    for line in lines:
        '''遍历列表的元素'''
        content += line
        '''将每个元素做字符串拼接，并赋给content'''
    print(content)
    '''打印拼接完成的字符串,获得π'''


'''方法二'''

file_name = 'pi_digits.txt'
'''将文件名称存储在变量file_name'''

with open(file_name) as file_object:
    '''打开文件'''
    lines = file_object.readlines()
    '''读取文件的每行作为元素存入列表'''
    print(lines)
    '''打印列表'''
    content = ''
    '''初始化变量content'''
    for line in lines:
        '''遍历列表的元素'''
        content += line.strip()
        '''将每个元素末尾的换行转义符祛除后做字符串拼接，并赋给content'''
    print(content)
    '''打印拼接完成的字符串'''


'''方法三'''

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()
    print(lines)
    content = "".join(lines)
    print(content)


'''方法四'''

file_name = 'pi_digits.txt'
'''将文件名称存储在变量file_name'''

with open(file_name) as file_object:
    '''打开文件'''
    content = ''
    '''初始化变量content'''
    for line in file_object:
        '''逐行读取文件的每一行内容'''
        content += line.strip()
        '''将每个元素末尾的换行转义符祛除后做字符串拼接，并赋给content'''
    print(content)
    '''打印拼接完成的字符串'''

