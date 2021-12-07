class Person:
   def __init__ (self, name="Name", age=0, pay=0, job=None):
       self.name = name
       self.age  = age
       self.pay  = pay
       self.job  = job

   def lastname(self):
       return self.name.split()[-1]

   def giveraise(self,percent):
       self.pay *= (1.0 + percent)
       return self.pay
