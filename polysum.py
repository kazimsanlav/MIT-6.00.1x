# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 17:53:31 2017

@author: kazIm
"""

def polysum(n, s):
    import math
    area = 0.25*n*s*s/math.tan(math.pi/n)
    return float("{0:.4f}".format(area))#to round up to 4 digit
