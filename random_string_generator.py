# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 12:47:39 2020

@author: Salman.Akhatar
"""
import string as asc_str
import time
class TheRandom:
    def __init__(self):
        self.string_uppercase = list(asc_str.ascii_uppercase)
        self.string_lowercase = list(asc_str.ascii_lowercase)
        self.string = None
    
    def generate_str(self, minimum=1, maximum=10, case=False):
        if case:
            pass
        else:
            pass
    
    def claculate_rand(self, maximum):
        tt = self.random_seed_from_time()
        seed = tt * 3
#        upper_limit = "1"
#        for _ in range(maximum-1):
#            upper_limit += "0"
#        print(upper_limit)
        t = seed * maximum
        m = self.random_seed_from_time()
        seed = t % m
        return seed, m
    
    def random_seed_from_time(self):
        tt = time.perf_counter()
        tt = str(tt)
        tt = tt.replace(".", "")
        tt = tt[:3]
        return int(tt)
    
    def generate_number(self, minimum=1, maximum=11):
        tt = time.perf_counter()
        tt = str(tt)
        tt = tt.replace(".", "")
        temp = []
        for _ in range(3):
            num, m = self.claculate_rand(maximum)
            temp.append((num, m))
        
        print(temp)
        un = ((temp[0][0]/temp[0][1])+(temp[1][0]/temp[1][1])+(temp[2][0]/temp[2][1]))%1
        return un

temp = TheRandom()
print(temp.generate_number(maximum=100))

#import random
#random.randint(1, 10)

#seed = 3
#for i in range(1, 20):
#    t = seed*i+1
#    seed = t % 100
#    print(seed)

