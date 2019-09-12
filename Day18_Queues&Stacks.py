# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:57:59 2019

@author: yusuke.aoki
"""
import sys

class Solution:
    # Write your code here
    def __init__(self):
        self.stack=[]
        self.queue=[]
    def pushCharacter(self,s):
        self.stack.append(s)
    def enqueueCharacter(self,s):
        self.queue.append(s)
    def popCharacter(self):
        return self.stack.pop()
    def dequeueCharacter(self):
        c=self.queue[0]
        self.queue.remove(c)
        return c
    


# read the string s
s=input()
#Create the Solution class object
obj=Solution()

l=len(s)

#push/enqueue all the characters of string s to stck
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome= True

for i in range(l//2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome=False
        break
if isPalindrome:
    print("The word, "+ s + ", is a palindrome.")
else:
    print("The word, "+ s + ", is not a palindrome.")
