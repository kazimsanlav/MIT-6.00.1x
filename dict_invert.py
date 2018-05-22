# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 09:50:53 2017

@author: kazIm
"""

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    keys=[]
    values=[]
    
    result={}
    for i in d:
        keys.append([i])
    for i in d:
        values.append(d[i])
       
    i = -1
    for v in values:
        i+=1
        result[v] = result.get(v,[]) + keys[i]
    return result        