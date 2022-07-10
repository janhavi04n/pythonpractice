"""
print first 16 numbers in binary, hex and octal
understanding binary, hexadecimal, octal
"""

# base 10
for i in range(17):
    print("{0:>2} in binary is {0:>2b}".format(i))

# base 16
for i in range(17):
    print("{0:>2} in hex is {0:>02x}".format(i))

# base 8
for i in range(17):
    print("{0:>2} in octal is {0:>02o}".format(i))

x = 0x20
y = 0x0a
print(x)
print(y)
print(x*y)