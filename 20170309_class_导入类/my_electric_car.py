#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:MingguiLu

'''从模块car中引入类ElectricCar
模块car中存储了多个类'''

from car import Battery,ElectricCar
'''从模块car导入多个类Battery,ElectricCar'''

my_tesla = ElectricCar('tesla','motel s',2017)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
'''注意，my_tesla使用类ElectricCar创建，而类Battery被作为ElectricCar的属性battery，所以调用类Battery的方法时，必须写为xxx.battery.xxx()'''
my_tesla.read_odometer()
my_tesla.fill_gas_tank()

print("\n")

my_le = Battery()
my_le.describe_battery()


