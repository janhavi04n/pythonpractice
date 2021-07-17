# -*- coding: utf-8 -*-
"""

"""
def sum_eo(n, t):
    sumof = 0
    if t == "e":
        for num in range(0, n, 2):
           sumof += num
    elif t == "o":
        for num in range(1, n, 2):
            sumof += num
    else:
        sumof = -1
        
    return sumof
        
        
sumeo = sum_eo(10, "e")
print(sumeo)

