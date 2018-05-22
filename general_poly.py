# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:17:35 2017

@author: kazIm
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    lent = len(L)
    def fun(x):
        import math
        result = 0
        for i in range(lent):
            result += L[i]*math.pow(x,lent-1-i)
        return result    
    return fun