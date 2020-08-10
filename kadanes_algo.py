# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:07:51 2020

PROBLEM_URL: https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0

@author: Salman.Akhatar
"""
def input_array(elements=0):
    temp = input("Input Array Elelments: ")
    temp = temp.split(" ")
    arr = [int(el) for el in temp]
    return arr


if __name__ == "__main__":
    testcases = int(input("Number of Testcases: "))
    
    sum_to_find = []
    values = []
    for i in range(testcases):    
        input_1 = input("Testcase Number {0}: ".format(i+1))
        input_1 = list(input_1.split(" "))
        input_1 = [int(el) for el in input_1]
        sum_to_find.append(input_1[1])
        temp = input_array(input_1[0])
        values.append(temp)