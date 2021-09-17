# -*- coding: utf-8 -*-
"""
understanding yield
yield keyword is used to return a value from a function
it differs from the return statement
Return - when return is used it means the end of the function
and subsequent call to the function will start the function from
scratch
Yield - this means the value is returned to the calling code
but the next call to the function will resume from where it left off
Such functions are generator functions
Generator functions are special type of iterators
they can be called as lazy iterators
example below
fibonacci_sequence is a generator function

"""
def fibonacci_sequence():
    prev, curr = 0,1
    
    while prev<=10:
        value = prev
        prev, curr = curr, prev+curr
        
        # call yield instead of return
        yield value
        
        
# call the generator function
# this will not return any value unless we call next() or iterate
# through it using a for loop
fib_sequence = fibonacci_sequence()

# this prints the type returned by fibonacci_sequence
print(fib_sequence)

# each call to next will call the fibonacci_sequence
# and the function will resume from yield
# so on first call of next it returns 0 which is assigned
# to the variable value
# the subsequent call to next 
# will return 1 which was assigned to prev in line 2 of while
# this will continue till the value of prev is <=10
# any further call to next will raise a StopIteration Error
# so in this example we need to call the next multiple times
# to get the value. Each call of next will resume the function
# from the previous state till the end of while/or any condition
# is reached 

# print(next(fib_sequence))
# print(next(fib_sequence))
# print(next(fib_sequence))
# print(next(fib_sequence))
# print(next(fib_sequence))
# print(next(fib_sequence))
# print(next(fib_sequence))
# print(next(fib_sequence))
# print(next(fib_sequence))
# print(next(fib_sequence))
# print(next(fib_sequence))


# to prevent the StopIteration Error we can also iterate over the
# generator using a for-loop

for i in fib_sequence:
    print(i)

# generator can also be created using a generator expression
# this is similar to list comprehension except the 
# comprehension logic is enclosed in paranthesis
# instead of square brackets
squares_gen = (x*x for x in range(1,11))
print(squares_gen)

# we can print the values in squares_gen either by calling
# next or using a for-loop
# using for-loop
for i in squares_gen:
    print(i)
