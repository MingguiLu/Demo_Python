#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:MingguiLu

class Dog():
    '''一次模拟小狗的简单尝试'''
    def __init__(self,name,age):
        '''初始化属性name和age'''
        self.name = name
        self.age = age

    def dog_description(self):
        '''描述小狗的基本信息'''
        print("This dog's name is "+self.name.title()+" and "+str(self.age)+" years old .")

    def site(self):
        '''模拟小狗被命令蹲下'''
        print(self.name.title()+" now is sitting !")

    def roll_over(self):
        '''模拟小狗被命令打滚'''
        print(self.name.title()+" now is roll over !")

taidy = Dog('wangcai',5)
'''根据类创建实例'''
taidy.dog_description()
'''调用方法'''
taidy.site()
taidy.roll_over()

print("\n")

guifei = Dog('xile',3)
guifei.dog_description()
guifei.site()
guifei.roll_over()

print("\n")

guifei.name = 'hehe'
'''访问属性'''
guifei.age = 4
guifei.dog_description()
guifei.site()
guifei.roll_over()

print("\n")


class Restaurant():
    '''一次模拟餐厅的尝试'''
    def __init__(self,restaurant_name,cuisine_type):
        '''初始化餐厅的属性'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        '''初始化就餐人数同时指定默认值'''

    def description_restaurant(self):
        '''描述餐厅信息'''
        print("This restaurant's name is "+self.restaurant_name.title()+" annd cuisine type is "+self.cuisine_type.title())

    def open_restaurant(self):
        '''餐厅在开门营业'''
        print(self.restaurant_name.title()+" now is openning !")

    def close_restaurant(self):
        '''餐厅已打烊下班'''
        print(self.restaurant_name.title()+" now is closing !")

    def read_number_served(self):
        '''在餐厅就餐总人数'''
        print("There are "+str(self.number_served)+" people eated here !")

    def set_number_served(self,number):
        '''修改餐厅就餐的总人数'''
        self.number_served = number

    def increment_number_served(self,number):
        '''递增餐厅就餐的总人数'''
        self.number_served += number

go_home_eat = Restaurant('回家吃饭','川菜')
go_home_eat.description_restaurant()
go_home_eat.open_restaurant()
go_home_eat.number_served = 234
go_home_eat.read_number_served()
go_home_eat.set_number_served(500)
go_home_eat.read_number_served()
go_home_eat.increment_number_served(130)
go_home_eat.read_number_served()

print("\n")

waipo_jia = Restaurant('外婆家','江浙菜')
waipo_jia.description_restaurant()
waipo_jia.close_restaurant()

print("\n")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['apple','banana','matcha','vanilla']

    def list_flavors(self):
        for i in self.flavors:
            print(i)

ice_cream_stand = IceCreamStand('snow stand','ice cream')
ice_cream_stand.description_restaurant()
ice_cream_stand.list_flavors()

print("\n")

class User():
    '''模拟一个用户欢迎界面'''
    def __init__(self,first_name,last_name,age,sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        '''描述用户信息'''
        describe = self.first_name.title()+" "+self.last_name.title()+" "+" is "+str(self.age)+" years old "
        if self.sex == '男':
            print(describe+"and is a 男人 !")
        else:
            print(describe+"and is a 女人 !")

    def greet_user(self):
        '''定制个性化的用户欢迎语'''
        if self.sex == '男':
            print("Welcome ! "+self.first_name.title()+"　先生！")
        else:
            print("Welcome ! "+self.first_name.title()+" 小姐 !")

    def read_login_attempts(self):
        '''描述用户登录次数'''
        print(self.first_name.title()+" "+self.last_name.title()+" attempt login "+str(self.login_attempts)+" times !")

    def increment_login_attemps(self,number):
        '''递增用户登录次数'''
        self.login_attempts += number

    def set_login_attemps(self,number):
        '''修改用户登录次数'''
        self.login_attempts = number

    def reset_login_attemps(self):
        '''重置用户登录次数'''
        self.login_attempts = 0

zhang_san = User('张','三',30,'男')
zhang_san.describe_user()
zhang_san.greet_user()
zhang_san.set_login_attemps(9)
zhang_san.read_login_attempts()

print("\n")

li_si = User('李','思',20,'女')
li_si.describe_user()
li_si.greet_user()
li_si.increment_login_attemps(1)
li_si.increment_login_attemps(2)
li_si.increment_login_attemps(5)
li_si.read_login_attempts()
li_si.reset_login_attemps()
li_si.read_login_attempts()

print("\n")

# user = User('','','','')
# '''模拟一个交互式的用户欢迎'''
# user.first_name = input("请输入first name:")
# user.last_name = input("请输入last name:")
# user.age = input("请输入年龄：")
# user.sex = input("请输入性别(男/女)：")ｐ
# user.describe_user()
# user.greet_user()

class Admin(User):
    def __init__(self,first_name,last_name,age,sex):
        super().__init__(first_name,last_name,age,sex)
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        for i in self.privileges:
            print(self.first_name.title()+" "+i+" !")

admin = Admin('admin','',0,'男')
admin.show_privileges()

print("\n")

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

new_car = Car('audi','A4',2016)
print(new_car.get_descriptive_name())
new_car.read_odometer()      # 获取汽车初始里程
new_car.odometer = 180      # 通过直接修改属性的值　设置汽车里程
new_car.read_odometer()
new_car.add_odometer(100)   # 调用方法，递增汽车里程
new_car.read_odometer()
new_car.sub_odometer(50)    # 调用方法，递减汽车里程
new_car.read_odometer()
new_car.update_odometer(300)    # 通过方法，修改汽车里程
new_car.read_odometer()
new_car.fill_gas_tank(10)

print("\n")

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

my_tesla =  ElectricCar('tesla','model s',2017)
print(my_tesla.get_descriptive_name())
my_tesla.update_odometer(400)
my_tesla.read_odometer()
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()




