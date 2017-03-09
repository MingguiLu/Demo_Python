#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:MingguiLu

'''导入整个模块,使用句点表示法访问需要访问的类
导入整个模块相对于导入模块中所有类的优点在于：
使用model_name.class_name语法来访问类，可以清楚地知道程序在哪些地方使用了导入的模块，还避免了导入模块中每个类可能引发的名称冲突'''
import car

my_beetle = car.Car('volkswagen','beetle',2016)
'''实例化类Car'''
print(my_beetle.get_descriptive_name())

print("\n")

my_le = car.Battery()
'''实例化类Battery'''
my_le.get_range()

print("\n")

my_tesla = car.ElectricCar('tesla','roadster',2017)
'''实例化类ElectricCar'''
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()

