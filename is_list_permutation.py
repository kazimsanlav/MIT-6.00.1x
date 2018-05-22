# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 11:33:08 2017

@author: kazIm
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
            
    *if L1 = ['a', 'a', 'b'] and L2 = ['a', 'b'] then is_list_permutation returns False
    *if L1 = [1, 'b', 1, 'c', 'c', 1] and L2 = ['c', 1, 'b', 1, 1, 'c'] then 
    is_list_permutation returns (1, 3, <class 'int'>) because the integer 
    1 occurs the most, 3 times, and the type of 1 is an integer 
    (note that the third element in the tuple is not a string).            
    '''
    dic_L1, dic_L2 = {},{}
    
    for i in L1:
        dic_L1[i] = dic_L1.get(i,0) + 1
    for i in L2:
        dic_L2[i] = dic_L2.get(i,0) + 1    
    
#    print(dic_L1)
#    print(dic_L2)
    
    if len(L1) != len(L2):
        return False
    for i in L1:
        if i not in L2:
            return False
    elem, times = None, 0    
    for i in dic_L1:
        if dic_L1[i] > times:
            times = dic_L1[i]
            elem = i
            
    return (elem, times, type(elem))   