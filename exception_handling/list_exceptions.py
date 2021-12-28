import sys


num_list = [1,2,3,4,5,6,7,8,9,10]
print(f"list {num_list}")
# this will break as we try to access an element from the list which does not exist
# i.e. if list size is 10 but we try to access element at index 15
# try except will not terminate with exit code 1 but log the error message and clean exit
print("getting values from a list")
try:
    idx = int(input("enter the index "))
    print(f"value at index {idx} is {num_list[idx]}")
except ValueError:
    print(f"Incorrect input .. pls try again")
except IndexError:
    print(f"size of list is {len(num_list)} .. you try to access value at {idx}")
except EOFError:
    sys.exit(1)

print("end")
