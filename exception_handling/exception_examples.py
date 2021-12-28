def factorial(n):
    """calculates n! using recursion"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


# function factorial calculates the factorial of a given number
# if the number is too large, then an exception is raised as
# the max depth of recursion is reached
# to handle it we need to enclose the code in a try/except

num = int(input("enter a number: "))
# here we call the factorial function by passing the entered number
# if the number is large then we see a RecursionError
# since the except is used the program will print the message and continue
# if we do not use try/except then the program terminates as soon as a exception is seen
try:
    print(factorial(num))
except RecursionError:
    print(f"cannot calculate the factorial of a large number {num}")

print("end of code")
