#!/usr/bin/env  python3

# the from looks for filename and then imports the class Student
from StudentPrivateProperty import Student

std = Student("Ramonski is the man")
print(dir(std))

print(std.name)

# with the @property-name.setter, it assigns name
std.name = 'Lucas'

print(std.name)

# with the @property-name.deleter, it allows deletion of property
del std.name

print(std._Student__schoolName)
# Will show that the method has been deleted
print(std.name)

print(dir(std))
