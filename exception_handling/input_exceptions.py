def div_nums(x, y):
    return x / y


try:
    x_val = int(input("enter a number : "))
    y_val = int(input("enter another number : "))
    print(f"divide {x_val} by {y_val}")
    print(div_nums(x_val, y_val))
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input .. please try again")

print("end of code")