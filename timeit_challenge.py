# we have 2 different functions to calculate the factorial of a number
# i.e. iteration and recursion
# using timeit module check which one is faster
# number of iterations in timeit to set at 1000 or 10000

import timeit


def factorial_iter(n):
    result = 1
    if n > 1:
        for f in range(2, n+1):
            result *= f
    return result


def factorial_recur(n):
    if n <= 1:
        return n
    else:
        return n * factorial_recur(n-1)


# x = factorial_iter(120)
# y = factorial_recur(120)
# print(x)
# print(y)

if __name__ == '__main__':
    print(timeit.timeit("x = factorial_iter(120)", setup="from __main__ import factorial_iter", number=1000))
    print(timeit.timeit("x = factorial_recur(120)", setup="from __main__ import factorial_recur", number=1000))
