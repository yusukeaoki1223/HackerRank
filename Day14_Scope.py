# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 17:24:28 2019

@author: yusuke.aoki
"""

#sample input
#3
#1 2 5
#sample output
#4


class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference=None

	# Add your code here
    def computeDifference(self):
        lengthElem=len(self.__elements)
        maxvalue=0
        for i in range(lengthElem):
            for j in range(lengthElem):
                value = abs(self.__elements[i]-self.__elements[j])
                if (maxvalue<value):
                    maxvalue=value
        self.maximumDifference=maxvalue


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)









