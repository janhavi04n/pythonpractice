# -*- coding: utf-8 -*-
"""
hacker rank solution
Given an integer,n , print the following values for each integer i from 1 to
n
:

    Decimal
    Octal
    Hexadecimal (capitalized)
    Binary


"""
number = int(input("enter a number : "))
width = len("{0:b}".format(number))


if not 1<=number<=99:
    print("please enter a number between 1 and 99")
else:
    for i in range(1, number+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))

