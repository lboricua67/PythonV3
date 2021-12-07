class Student:
   # Private methods have double underscore
   __schoolName = 'Tuley Middle School'    # private class attribute


   def __init__(self, name, age):
      self.__name=name        # private instance attribute
      self.__salary=age

   def __display(self):       # private method
       print('This is a private affair')
