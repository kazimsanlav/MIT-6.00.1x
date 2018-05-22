# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:04:15 2017

@author: kazIm
"""
res=[]
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
    is flattened into [1,'a','cat',2,3,'dog',4,5]
    '''  
    for elm in aList:
       if type(elm) != list:
           res.append(elm)
       else:#if it is a list
           flatten(elm)
    return res 