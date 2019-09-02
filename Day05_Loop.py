# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 01:33:25 2019

@author: yusuke.aoki
"""


import math
import os
import random
import re
import sys

n = int(input())
for i in range(1,11):
    k=n*i
    print(str(n)+"x"+str(i)+"="+str(k))