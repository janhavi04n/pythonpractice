def my_range(n: int):
    print("starting m_range")
    start = 0
    while start<n:
        yield start
        start += 1


my_vals = my_range(10)
print("created a generator {}".format(my_vals))

# for val in my_vals:
#     print("val {}".format(val))


print(next(my_vals))
print(next(my_vals))
print(next(my_vals))
print(next(my_vals))
print(next(my_vals))
print(next(my_vals))
print(next(my_vals))
print(next(my_vals))
print(next(my_vals))
print(next(my_vals))
# next line will raise a StopIteration error
# print(next(my_vals))
