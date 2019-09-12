# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:22:30 2019

@author: yusuke.aoki
"""


#!/bin/python3

import sys


S = input().strip()

try:
    k=int(S)
    print(S)
except BaseException as error:
    print("Bad String")


