# -*- coding: utf-8 -*-
"""

reads a numeric input
print the factorial of the number

"""

def factorialof(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return (num * factorialof(num-1))


num = int(input("enter a number : "))

isValid = (num>=0)

if isValid:
    print('factorial of {0} is {1}'.format( num, factorialof(num)))
else:
    print('enter number >=0')




