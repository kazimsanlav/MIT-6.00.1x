# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 11:45:57 2017

@author: kazIm
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    sum = 0
    for i in range(len(listA)):
        sum += (listA[i]*listB[i])
    return sum    