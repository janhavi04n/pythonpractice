# -*- coding: utf-8 -*-
"""
uderstanding the itertools module
"""
import itertools

numbers = [i for i in range(1,6)]
print(numbers)

# this returns a generator
permutatons = itertools.permutations(numbers)
print(permutatons)
# print all the permutations of the numbers list
print(list(permutatons))

combi = itertools.combinations(numbers, 3)
print(combi)
# combinations of the number list - 3 numbers in each combination
print(list(combi))
