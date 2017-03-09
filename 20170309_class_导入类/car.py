#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:MingguiLu

'''在一个模块中存储多个类'''

class Car():
    '''描述汽车信息的类'''
    def __init__(self,make,model,year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        '''给属性指定默认值，在方法_init_()初始化时无需包含为它提供初始值的形参'''

    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = self.make+" "+self.model+" "+str(self.year)
        return long_name.title()

    def read_odometer(self):
        '''打印一条指出汽车里程的消息'''
        print("This car has "+str(self.odometer)+" miles on it")

    def add_odometer(self,add_mile):
        '''增加汽车的里程'''
        self.odometer += add_mile

    def sub_odometer(self,sub_mile):
        '''减少汽车的里程'''
        self.odometer -= sub_mile

    def update_odometer(self,update_odometer):
        '''重设汽车的里程'''
        self.odometer = update_odometer

    def fill_gas_tank(self,litre):
        print("This car has "+str(litre)+" L gas in it .")


class Battery():
    '''模拟电动汽车电瓶'''
    def __init__(self,battery_size=70):
        '''初始化电瓶的属性'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''打印一条描述电瓶容量的消息'''
        print("This car has a "+str(self.battery_size)+"-KWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately "+str(range)
        message += " miles on a full charge."
        print(message)


'''类的继承''' '''将实例用作属性'''
class ElectricCar(Car):
    '''电动车特有之处'''
    def __init__(self,make,model,year):
        '''初始化父类的属性'''
        super().__init__(make,model,year)
        '''将父类和子类关联起来，父类也被称为超类(superclass)'''
        self.battery = Battery()
        '''将实例Battery()用作ElectricCar()类的一个属性'''

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank !")