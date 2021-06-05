# -*- coding: utf-8 -*-
"""
hacker rank tuples

Given an integer, , and space-separated integers as input, create a tuple, t , 
of those n integers. Then compute and print the result ofhash(t)

"""

n = int(input())

integer_list = map(int, input().split())

integer_tuple = tuple(integer_list)
isValid = len(integer_tuple) == n

if isValid:
    print(hash(integer_tuple))