# -*- coding: utf-8 -*-
"""
Created on Sat May  1 18:37:00 2021

@author: Janhavi
"""

# slice has 3 params i.e start, stop, step
# start at startIndex, slice up to but not including stopIndex
# by default step = 1

str = 'This is a string for testing'
print(str[2:8])

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0:15:2])

backwards = letters[25::-1]
print(backwards)

# print qpo
print(letters[-10:-13:-1])
print(letters[16:13:-1])

# print edcba
print(letters[4::-1])

# print last 8 characters in reverse order
print(letters[25:17:-1])
print(letters[:-9:-1])



print("Hello " * 5)







quantity = 10
price = 5.0
total = quantity * price
tax = total / 5
 
Total = total + tax
 
print(total)