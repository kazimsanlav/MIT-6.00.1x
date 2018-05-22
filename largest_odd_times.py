# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 09:28:04 2017

@author: kazIm
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Your code here
    result = None
    dicL={}
    for i in L:
        dicL[i] = dicL.get(i,0) + 1
    print (dicL)    
    if dicL[max(dicL)] % 2 == 1:
        result = max(dicL)
    print(result)    
    