# Python program to show that the variables with a value
# assigned in class declaration, are class variables
 
# Class for Computer Science Student
class CSStudent:
    stream = 'cse'                  # Class Variable
    def __init__(self,name,roll):
        self.name = name            # Instance Variable
        self.roll = roll            # Instance Variable
 
# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)
c = CSStudent('Ramon', 3)
 
print(a.stream)  # prints "cse"
print(b.stream)  # prints "cse"
print(c.stream)  # prints "cse"
print("---------------------------------------------------------------------") 
print(a.name)    # prints "Geek"
print(b.name)    # prints "Nerd"
print(c.name)    # prints "Ramon"
print("---------------------------------------------------------------------") 
print(a.roll)    # prints "1"
print(b.roll)    # prints "2"
print(c.roll)    # prints "3"
print("---------------------------------------------------------------------") 
# Class variables can be accessed using class
# name also
print(CSStudent.stream," this is was was originally in stream class") # prints "cse"
print("---------------------------------------------------------------------") 
 
# Now if we change the stream for just a it won't be changed for b
a.stream = 'ece'
print(a.stream," this is after a object was initialize") # prints 'ece'
print(b.stream," wasn't changed so it matches class value ") # prints 'cse'
print(c.stream," wasn't changed so it matches class value ") # prints 'cse'
 
print("---------------------------------------------------------------------") 
# To change the stream for all instances of the class we can change it
# directly from the class
CSStudent.stream = 'mech'

print(a.stream," matches the assigned value") # prints 'ece'
print(b.stream," matches the class value after assignment of class") # prints 'mech'    # <== Since b object was never changed, it uses whatever was define at class level
print(c.stream," matches the class value after assignment of class") # prints 'mech'    # <== Since c object was never changed, it uses whatever was define at class level
