"""
learn to use the map function
map() - returns a map object (which is an iterator)
map(function, iterable, ...)
applies the function to each element of the iterable
and returns an iterator. This iterator can then be passed
in list(), set()
Multiple iterables can be passed to map function
"""
def square(num):
    return num*num

numbers = [i for i in range(1,21)]

# here map(square, numbers)
# means square function will be called for each element in numbers
squares = map(square, numbers)

list_of_squares = list(squares)
print(list_of_squares)
#for sqr in list_of_squares:
#    print(sqr)