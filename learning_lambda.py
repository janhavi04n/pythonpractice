# -*- coding: utf-8 -*-
"""
basics:
    understanding LAMBDA
    a. anonymus functions.
    b. does not require a function name, def keyword - anything
        that is required for a python function
    c. Cannot be used for complex tasks.
    d. Requires a single line of code
    e. returns a function object
    f. keyword `lambda` is used instead of def
    g. syntax is: lambda arguments : expression
    e.g. sqr = lambda x : x*x
    above is a lambda function where x is the argument, and x*x is
    the expression
    when it gets evaluated it returns the x*x
    print(sqr(2)) // 4 
"""
from functools import reduce


# first we create a list of all numbers in in range 1 to 50
numbers = [i for i in range(1, 101)]
print(len(numbers))

# next we see the filter function
# let us check the even numbers
# here we pass the lambda function to a filter
# function runs on each element of the numbers list
# returns True if even number
evens = filter(lambda i : i%2 ==0, numbers)
print(evens)
# above print statement will return a filter object
# this has to be cast to a list to check the elements, length etc
print(f"total even numbers between 1 and 100 {len(list(evens))}")


# sometimes lambda can be something simple as returning a cube 
# of a number
# we can do this using a function which takes a int input and returns
# the cube of the int
# lambda gives us an option to write the same code with just one line
# instead of defining a function
cube = lambda x : x*x*x
print(cube(3))

# we can also use lambda in a map function
# map parameters are function, *iterable
# map will execute the function with each element of the iterable
# we can pass a lambda instead of function name to map
# first lets create a simple list of even numbers 
even_numbers = [i for i in range(21) if i%2 == 0]
square = map(lambda x : x*x, even_numbers)
print(square)
print(list(square))

# using lambda in reduce
# reduce is present in functools module so we need to import it
one_to_ten = [i for i in range(1, 11)]
sum_of = reduce(lambda x,y : x+y, one_to_ten)
print(sum_of)


# this is from w3schools
# lambda can be used as an anonymus function inside another function
# below myfunc takes 1 argument `n` and this argument is then
# multiplied by another unknown number

def myfunc(n):
    return lambda a: a*n


double = myfunc(2)
print(double(5))

triple = myfunc(3)
print(triple(5))