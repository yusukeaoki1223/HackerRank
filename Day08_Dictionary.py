# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:47:51 2019

@author: yusuke.aoki
"""

# sample input
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

#sample output
sam=99912222
Not found
harry=12299933


phonebook={}
num=int(input())


for i in range(0,num):
    entry=str(input()).split(" ")
    name=entry[0]
    number = int(entry[1])
    phonebook[name]=number

for i in range(0,num):
    name = input()
    if name in phonebook:
        print(name + "=" + str(phonebook[name]))
    else:
        print("Not found")


phonebook['sam']
