import os

class DirInfo:
   # Private methods have double underscore
   __DirectCurrPath = os.getcwd()

   def __init__(self, CurrPath):
      self.__CurrPath=CurrPath        # private instance attribute

   @property
   def CurrPath(self):
       return self.__CurrPath

   @CurrPath.setter               # property-CurrPath.setter decorator
   def CurrPath(self, value):
       print(value)
       self.__CurrPath = value

