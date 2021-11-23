from oops_props_deco import Student
from inheritence import Bike, Car


stu = Student('stuart', 5, 58)

print(stu)

stu.grade = 6
print(stu)

# will call the setter
stu.marks = 59
print(stu)

# will calls the getter
print(stu.marks)


yamaha = Bike("Yamaha", "250cc")
print(yamaha)
print(yamaha.show_details())

honda = Car("Honda city")
print(honda)
# below line will displat TypeError as only the last defined
# make_sound method of Car class can be available
# other 2 are not available as overloadig is not available in python
# honda.make_sound("beep", 20)
honda.make_sound()
