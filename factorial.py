# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 11:26:28 2020

@author: Salman.Akhatar
"""
def fact(n):
    if n < 0:
        return "Invalid Number"
    elif n == 0 or n == 1:
        return n
    else:
        return n * fact(n-1)

fact(6)