# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 11:35:20 2017

@author: kazIm
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    import math
    i1 = int(math.log(num, base))
    i2 = i1+1
#    print(i1,i2)
    if abs(base**i1 - num) <= abs(base**i2 - num):
        return i1
    return i2