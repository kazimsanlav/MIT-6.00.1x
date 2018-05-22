# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 09:07:43 2017

@author: kazIm
"""

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    vowels_lower = ['a', 'e', 'i', 'o', 'u']
    vowels_upper = list("".join(vowels_lower).upper())
    vowels = vowels_lower + vowels_upper
    
    result=""
    for ch in s:
        if ch not in vowels:
            result += ch
    print(result)