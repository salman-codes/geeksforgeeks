# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:50:18 2020

PROBLEM URL: https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

@author: Salman.Akhatar
"""
def find_subarray(array, to_find):
    for i in range(len(array)):
        for j in range(len(array)-1):
            t = j+1
            temp = sum(array[i:t])
            if temp == to_find:
                return i+1, t
    
    return -1

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
    
    for vals, find_sum in zip( values, sum_to_find):
        result = find_subarray(vals, find_sum)
        print(result)
    
    