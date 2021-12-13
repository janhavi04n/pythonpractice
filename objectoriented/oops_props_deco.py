# -*- coding: utf-8 -*-
"""
understanding properties
decorators
"""


class Student(object):

    def __init__(self, name, grade, marks):
        self.name = name
        self._grade = grade
        self._marks = marks
        # use the _property to tell other developers
        # this is a private field

    def _get_grade(self):
        return self._grade

    def _set_grade(self, grade):
        self._grade = grade

    # this will create a property grade and call the getter
    # and setter
    grade = property(_get_grade, _set_grade)

    # another way of creating the property is by decorators
    # so instead of property(...) we can use the annotations
    # as given below
    # the name of the method should be the name of the property
    # these are called decorators

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, marks):
        self._marks = marks

    def __str__(self):
        return "Student [Name: {0.name}, Grade: {0.grade}, Marks: {0.marks}]".format(self)

    def show_results(self):
        pass

# =============================================================================
#     def go_to_school(self, func):
#         def wrapper():
#             if 8 <= datetime.now().hour < 13:
#                 func()
#             else:
#                 print("do your homework")
#             
#         return wrapper
#         
#     
#     def go_to_school():
#         print("at school")
# =============================================================================
