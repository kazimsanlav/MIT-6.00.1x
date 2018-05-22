# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 09:06:37 2017

@author: kazIm
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    import math
    a = int( math.sqrt(k*2))
    b = a+1
    print("a: ", a)
    print("b: ", b)
    print("k: ", k)
    
    if a*b == k*2:
        return True
    return False