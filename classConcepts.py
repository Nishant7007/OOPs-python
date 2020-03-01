#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 17:11:53 2020

@author: ictd
"""

class Circle():
    
    pi=3.14
    
    def __init__(self,radius=1):
        self.radius=radius
    
    def area(self):
        return self.radius * self.radius * Circle.pi
    
    def change_radius(self,radius):
        self.radius=radius
    
        
myobj=Circle(radius=3)
print(myobj.radius)
print(myobj.area())

myobj.change_radius(400)

print(myobj.radius)
print(myobj.area())
    