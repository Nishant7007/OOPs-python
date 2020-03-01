#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 09:35:37 2020

@author: ictd
"""

class Animal():
    
    def __init__(self):
        print("this is an animal class")
        
    def eat(self):
        print("Animal is eating")
        
        
class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("this is a dog class")
        
    def eat(self):
        print("dog is eating")
        
    
dog1=Dog()

dog1.eat()