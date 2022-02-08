# -*- coding: utf-8 -*-
"""
Created on Sat May  1 12:47:37 2021

@author: Janhavi
"""



year = int(input('Enter the year: '))
#print('You entered '+year)

is_leap = (year % 4 == 0 and (year % 400 == 0 or year % 100 != 0))

if is_leap:
    print('{} is a leap year'.format(year))
else:
    print('{} is not a leap year'.format(year))