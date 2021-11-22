from oops_props_deco import Student


stu = Student('stuart', 5, 58)

print(stu)

stu.grade = 6
print(stu)

# will call the setter
stu.marks = 59
print(stu)

# will calls the getter
print(stu.marks)