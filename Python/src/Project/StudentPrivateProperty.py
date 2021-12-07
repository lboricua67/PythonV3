class Student:
   # Private methods have double underscore
   __schoolName = 'Tuley Middle School'    # private class attribute

   def __init__(self, name):
      self.__name=name        # private instance attribute

   @property
   def name(self):
       return self.__name

   @name.setter               # property-name.setter decorator
   def name(self, value):
       self.__name = value

   @name.deleter              #property-name.deleter decorator
   def name(self):
       print('Deleting...', self.__name)
       del self.__name
