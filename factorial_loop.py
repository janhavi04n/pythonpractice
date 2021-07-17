# -*- coding: utf-8 -*-
"""
Prints the factorial of first n numbers

@author: Janhavi
"""
def factorialof(num: int) -> int:
    """
    

    Parameters
    ----------
    num : int
        get the factorial of this number.

    Returns
    -------
    int
        factorial.

    """
    if (num == 0 or num == 1):
        return 1
    else:
        return (num * factorialof(num-1))


for num in range(0, 36):
    print("{} {}".format(num, factorialof(num)))