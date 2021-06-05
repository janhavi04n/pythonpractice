# -*- coding: utf-8 -*-
"""

hacker rank - swap case
You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters 
and vice versa.

constraints
0<=len(s)<=1000

"""

s = input("enter a string ")

valid = (0<=len(s)<=1000)

if valid:
    print(s.swapcase())

