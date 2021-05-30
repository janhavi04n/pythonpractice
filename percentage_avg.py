# -*- coding: utf-8 -*-
"""
hacker rank- find the avg
The provided code stub will read in a dictionary containing key/value pairs
of name:[marks] for a list of students.
Print the average of the marks array for the student name provided,
showing 2 places after the decimal.
"""
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

isValid = (2<=n<=10)
   
if isValid:    
    if query_name in student_marks.keys():
        mymarks = student_marks[query_name]
        if len(mymarks) == 3:
            sum_marks=0
            for marks in mymarks:
                sum_marks+=marks
            avg = sum_marks/3
            print("{:.2f}".format(avg))
    
