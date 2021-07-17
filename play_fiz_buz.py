# -*- coding: utf-8 -*-
"""
udemy exercise

if number is divisible by 3 - fizz
if divisible by 5 - buzz
divisible by both - fizz buzz
else return number

"""

def fizz_buzz(num: int) -> str:
    """
    

    Parameters
    ----------
    num : int
        number to check if divisible by 3 or 5 or both or none.

    Returns
    -------
    str
        fizz if divisible by 3
        buzz if divisible by 5
        fizzbuzz if divisible by both 3 and 5
        number if not divisible by either.

    """
    if num % 3 ==0 and num % 5 ==0:
        return "fizz buzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)


for num_to_check in range(1, 101):
    print(fizz_buzz(num_to_check))
