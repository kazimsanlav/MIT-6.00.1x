# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 11:48:34 2017

@author: kazIm
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    
    L = [[1, 2], [3, 4], [5, 6, 7]] then 
    deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]
    
    """
    L2 =[]
    L = L[::-1]
    for each in L:
        each = each[::-1]
        L2.append(each)
    print(L2)