# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:53:05 2019

@author: yusuke.aoki
"""

#sample input
#The Alchemist
#Paulo Coelho
#248

#sample output
#Title: The Alchemist
#Author: Paulo Coelho
#Price: 248
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author, price):
        super().__init__(title,author)
        self.price=price
    
    def display(self):
        print("Title: " + title)
        print("Author: " + author)
        print("Price: " + str(price))

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
