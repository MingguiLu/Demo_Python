#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:MingguiLu


def greet_user():
    '''显示简单的问候语'''
    print('Hello ! Welcome !')

greet_user()

def greet_user(username):
    '''显示简单的问候语'''
    print('Hello ! Welcome!'+username.title()+' .')

greet_user('Minggui Lu')

def display_messages(section) :
    '''显示本章所学的内容'''
    print('我正在学习'+section.title()+'.')

display_messages('function')

def favorite_book(title):
    '''显示我最喜欢的书籍之一'''
    print('One of my favorite books is '+title.title()+' .')

favorite_book('Alice in Wonderland')

def describe_pet(animal_type,pet_name):
    '''显示宠物的信息'''
    print("I have a "+animal_type+".")
    print('My '+animal_type+"'s name is "+pet_name.title()+".")

describe_pet('cat','kitty')
describe_pet('dog','wangcai')
describe_pet(animal_type="pig",pet_name="dapang")
describe_pet(pet_name="dapang",animal_type="pig")

def describe_pet(pet_name,animal_type="dog"):
    '''显示宠物信息，默认宠物类型为dog'''
    print("I have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")

describe_pet('wangcai')
describe_pet('wangcai','cat')
describe_pet(pet_name="miemie",animal_type="sheep")

'''调用函数时缺少实参我会发生错误'''
# describe_pet()

def make_shirt(size,font="I love python"):
    '''说明Ｔ恤的大小和印字'''
    print("I want a Ｔ恤 "+str(size)+" big and with "+"'"+font.title()+"' .")

make_shirt(180)
make_shirt(175,'404 not found')

def describe_city(city,country="China"):
    '''描述城市所属的国家信息'''
    print(city.title()+" is in "+country+".")

describe_city('wuhan')
describe_city('New York','USA')
describe_city(country='France',city="Paris")

def get_formatted_name(first_name,last_name):
    '''返回格式化的姓名'''
    full_name = first_name+" "+last_name
    return full_name.title()

name = get_formatted_name('Minggui','Lu')
print(name)

def get_formatted_name(first_name,last_name):
    '''返回格式化的姓名'''
    return first_name+" "+last_name

name = get_formatted_name('Lu','minggui')
print(name)

def get_formatted_name(first_name,last_name,middle_name=''):
    '''显示格式化的姓名'''
    if middle_name:  #当middle_name为非空时，把middle_name也加入full_name
        full_name = first_name+" "+middle_name+" "+last_name
    else:   #当middle_name为空时，full_name不包含middle_name
        full_name = first_name+" "+last_name
    return full_name

name = get_formatted_name("lu",'minggui')
print(name)
name = get_formatted_name("lu","minggui","kind")
print(name)


def bulid_person(first_name,last_name):
    person = {'first':first_name,'last':last_name}
    return person

username = bulid_person('minggui','lu')
username = bulid_person('long','li')
print(username)


