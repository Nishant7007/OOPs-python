#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 09:53:48 2020

@author: ictd
"""


class Book():
    
    
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
        
    def __str__(self):
        return "Title: {}\nAuthor: {}\nPages:{}".format(self.title,self.author,self.pages)
    
        
        
book=Book('class concepts','jose',200)
print(book)
