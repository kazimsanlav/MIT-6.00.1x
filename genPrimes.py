# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 10:08:10 2017

@author: kazIm
"""

def genPrimes():
    primes = [2]
    prime = True
    add = False
    x = 2
    yield primes[-1]
    while True:
        while not add:
            for p in primes:
                if (x % p) == 0:
                    prime = False
            if prime:
                primes.append(x)
                add = True 
            x += 1
            prime = True
        yield primes[-1]
        add = False