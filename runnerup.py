# -*- coding: utf-8 -*-
"""
hacker rank - find runnerup score

Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given n scores. 
Store them in a list and find the score of the runner-up.

"""

n = int(input())
arr = map(int, input().split())


scores = list(sorted(set(arr)))
print('printing runner up score')
print(scores[len(scores)-2])

