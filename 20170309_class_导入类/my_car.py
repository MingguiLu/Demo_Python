#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:MingguiLu

'''导入单个类'''

from car import Car
'''从模块car中导入类Car'''

my_car = Car('honda','city',2016)
print(my_car.get_descriptive_name())
my_car.fill_gas_tank(250)
my_car.set
