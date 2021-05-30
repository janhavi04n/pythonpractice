# -*- coding: utf-8 -*-
"""
hacker rank- nested lists
Given the names and grades for each student in a class of N students,
store them in a nested list and print the name(s) of any student(s)
having the second lowest grade.
"""

studentscores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    studentscores.append([name, score])

scoresmap = dict(studentscores)

scores = sorted(set(scoresmap.values()))
second_lowest_score = scores[1]

second_name = [nm for nm,scr in scoresmap.items() if scr==second_lowest_score]

second_name=sorted(second_name)
for name in second_name:
    print(name)
        
