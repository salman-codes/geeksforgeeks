# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:41:55 2020

@author: Salman.Akhatar
"""
from factorial import fact

def combinations(n, r):
    if n < r:
        return 0
    fact_n = fact(n)
    fact_r = fact(r)
    fact_n_minus_r = fact(n-r)
    
    result = fact_n / (fact_r * fact_n_minus_r)
    return result


t = "#" * 120 +"\n"
te = t+"Testing the Ouptut of Strng format\n"+t

