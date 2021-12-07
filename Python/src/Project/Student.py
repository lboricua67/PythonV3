class Student:
   _schooName = 'Tuley Middle School'    # protected class attribute


   def __init__(self, name):
      self._name=name        # protected instance attribute

   @property
   def name(self):
      return self._name

   @name.setter
   def name(self, newname):
       self._name = newname
