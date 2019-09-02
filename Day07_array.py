# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:29:18 2019

@author: yusuke.aoki
"""


import math
import os
import random
import re
import sys

n = int(input())

arr = list(map(int, input().rstrip().split()))

temp=arr[::-1]

print( " ".join( repr(e) for e in temp ) )

