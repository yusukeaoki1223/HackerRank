# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 01:36:24 2019

@author: yusuke.aoki
"""


N=int(input())

for i in range(0,N):
    
    S=input()
    for j in range(0,len(S)):
        if j % 2 ==0:
            print(S[j],end='')
            
    print(" ", end='')
    
    for j in range(0,len(S)):
        if j % 2 !=0:
            print(S[j],end='')
            
    print("")
