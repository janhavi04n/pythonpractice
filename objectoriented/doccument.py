# -*- coding: utf-8 -*-
"""
learning object oriented
"""


class Document(object):
    paper_type = 'handmade paper'

    def __init__(self, pages, size):
        self.pages = pages
        self.size = size
        
    def print_me(self, value_to_print):
        print(f"printing on {self.paper_type} paper: {value_to_print}")


a4doc = Document(100, 'A4')
a3doc = Document(25, 'A3')

print(f"Created {a3doc.size} document with {a3doc.pages} pages")
# in python we can add attributes to any particular instance dynamicaly
a4doc.colour = 'black'
print(f"Created {a4doc.size} book with {a4doc.pages} pages of {a4doc.colour} colour")
# following line will return a AttributeError as colour attribute is only
# availavle to a4doc instance
# print(f"{a3doc.colour}")
print(Document.paper_type)
print(a3doc.paper_type)
print(a4doc.paper_type)
# above prints the value of page_type variable which is a class variable
# this variable is shared by all instances of the class
# any change to this is reflected in all the instances
Document.paper_type = 'yupo paper'
print(Document.paper_type)
print(a3doc.paper_type)
print(a4doc.paper_type)
# in above example change is made in one place but all instances show updated
# value for page_type
# but modifying the variable value on any instance is reflected in that
# instance only
a3doc.paper_type = 'synthetic paper'
print(Document.paper_type)
print(a3doc.paper_type)
print(a4doc.paper_type)
# above prints synthetic paper only for a3doc but other 2 are still digital
# this is similar to shadowing a global varaible inside a function
# when this is done then python will create a page_type inside the a3doc
# namespace and a3doc instance will refer to this value in the prgogram
a3doc.print_me("hello object oriented python")
Document.print_me(a4doc, "another way of calling method")