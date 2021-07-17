# -*- coding: utf-8 -*-
"""
coding practice
"""
def sum_of_args(*values: float) -> float:
    """
    calculate the sum of all the numbers passed as arguments

    Parameters
    ----------
    *values : float
        list of values

    Returns
    -------
    float
        sum of all the values.

    """
    sum = 0
    for i in values:
        sum+=i
        
    return sum


print(sum_of_args(1,2,3))
print(sum_of_args(8,20,2))
print(sum_of_args(12.5, 3.147, 98.1))
print(sum_of_args(1.1, 2.2, 5.5))