# -*- coding: utf-8 -*-
"""
object orirnted
inheritence
"""
class Vehicle(object):
    def __init__(self, name, no_of_wheels=2):
        self.name = name
        self.no_of_wheels = no_of_wheels
        
        
    def __str__(self):
        return "Vehicle [Name: {0.name}, No of Wheels: {0.no_of_wheels}".format(self)
        
    
class Bike(Vehicle):
    def __init__(self, name, capacity):
        super(Bike, self).__init__(name=name, no_of_wheels=2)
        # this will call the __init__ of the super class Vehicle
        # this is needed cos once we define the init in a subclass
        # it shadows the super init and does not call it
        # so we need to call super class init explicit call
        self.capacity=capacity
        
    def show_details(self):
        return "This is a {0.name} Bike of capacity {0.capacity}".format(self)
    
    
class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name=name, no_of_wheels=4)
        # this is another way of calling super
        # instead of passing ClassName, self as
        # parameters
        
 
        
# there is no overloading concept in python
# if we define multiple methods with same name in a class
# then python will only recognse the one added last
# in below examples we can access only make_sound(self)
# if we try to access the other 2 methods then we get the following error
# TypeError: make_sound() takes 1 positional argument but 3 were given
    def make_sound(self, sound):
        print(sound)
    
    def make_sound(self, sound, times):
        print(sound*times)
        
    def make_sound(self):
        print("beep")
        