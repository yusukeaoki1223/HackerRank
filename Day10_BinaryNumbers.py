# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:48:48 2019

@author: yusuke.aoki
"""

#!/bin/python3

import math
import os
import random
import re
import sys


n = int(input())
result=0
maximum=0

while n>0:
    if n % 2 ==1:
        result +=1
        if result>maximum:
            maximum=result
    
    else:
        result =0
    n //=2
print(maximum)
        