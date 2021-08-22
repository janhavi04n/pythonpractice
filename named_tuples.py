# -*- coding: utf-8 -*-
"""
understanding named tuples
"""
from collections import namedtuple


# this is one of the ways to create a named tuple
# creating named tuple by passing field names as space separated string
Student = namedtuple("Student", "fname lname classes")
student = Student("John", "Doe", ["maths", "physics", "history"])
print(id(student))
print(student)
print(type(student))

# named tuple is immutable
# elements of the named tuple can be accessed thru index and named fields
print(student.fname)
print(student.lname)
print(student[0])
print(student[2])

# named tuple is immutable but its elements can be mutable
student.classes.append("economics")
print(student.classes)

# creating named tuple by passing the field names as comma separated string
Point = namedtuple("Point", "x, y")
point = Point(5, 8)
print(point)

# creating named tuple by passing field names as a iterable
Point = namedtuple("Point", ["x", "y"])
point = Point(3, 9)
print(point)

# creating named tuple with generator for field names
Point = namedtuple("Point", (field for field in "xy"))
point = Point(4, 7)
print(point)

# field names cannot be python keywords and should not start with _
# this returns ValueError: Field names cannot start with an underscore
# Point = namedtuple("Point", "x _y")
