# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:48:35 2020

PROBLEM URL: https://practice.geeksforgeeks.org/problems/count-the-triplets/0

@author: Salman.Akhatar
"""
def validate_triplet(arr):
    
    return False

def find_triplets(array):
    counter = 0
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            t = j+1
            if validate_triplet(array[i:t]):
                counter += 1
    if counter:
        return counter
    return -1


def input_array(elements=0):
    temp = input("Input Array Elelments: ")
    temp = temp.split(" ")
    arr = [int(el) for el in temp]
    return arr

if __name__ == "__main__":
    testcases = int(input("Number of Testcases: "))
    
    values = []
    for i in range(testcases):    
        input_1 = int(input("Testcase Number {0}: ".format(i+1)))
        temp = input_array(input_1)
        values.append(temp)
    
    for vals in values:
        result = find_triplets(vals)
        print(result)
    
