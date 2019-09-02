# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:25:51 2019

@author: yusuke.aoki
"""

# fatorial

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n>1:
       return n*factorial(n-1)
    else:
       return 1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()