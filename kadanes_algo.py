# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:07:51 2020

PROBLEM_URL: https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0

@author: Salman.Akhatar
"""
def find_subarr(arr):
    temp = 0
    for val in arr:
        temp += val
        if temp < val:
            temp -= val
    
    if not temp:
        return arr[0]
    return temp

def input_array():
    temp = input("Input Array Elelments: ")
    temp = temp.split(" ")
    arr = [int(el) for el in temp]
    return arr


if __name__ == "__main__":
    testcases = int(input("Number of Testcases: "))
    
    array = []
    for i in range(testcases):    
        num_of_elms = input("No. f Elements in TC {0}: ".format(i+1))
        num_of_elms = int(num_of_elms)
        temp = input_array()
        array.append(temp[:num_of_elms])
    
    for arr in array:
        print(find_subarr(arr))

