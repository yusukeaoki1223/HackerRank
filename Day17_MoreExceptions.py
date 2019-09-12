# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:32:52 2019

@author: yusuke.aoki
"""

class Calculator:
    def power(self,n,p):
        if(n<0 or p<0):
            raise Exception("n and p should be non-negative")
        else:
            return pow(n,p) #階乗

myCalculator=Calculator()

T=int(input())

for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)  

