# -*- coding: utf-8 -*-
"""
learning about decorators in python
Simple example to demonstrate decorators in python
decorators are mainly used when you need to change the behaviour
of a function without changing the function
e.g. log the start and end time and total time taken by a function
this can also be reused hence avoid duplicating of code
below example is from freecodecamp.org

to create a decorator function:
    1. create a outer function that takes a name of function (say `func`) 
        as parameter
    2. create a inner function as a wrapper. we will call the `func` from
        here
    3. return the inner func
    4. to use this decorator function place this function above the 
        function we are calling with @ prefix
    E.g. if decorator function name is my_decorator_func, then 
    use @my_decorator_func above the function which we will call
"""
from datetime import datetime


''' in this example we create a decorator which will log the datetime
    when the function was executed '''
    
def date_logger(func):
    def wrapper():
        print(f"function {func.__name__} was executed at {datetime.today().strftime('%d-%m-%Y %H:%M:%S')}")
        func()
    return wrapper



if __name__ == '__main__':
    @date_logger
    def test_func():
        print("testing decorators")
        
        
    test_func()
