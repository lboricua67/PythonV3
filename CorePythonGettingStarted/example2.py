#int
#float
#NoneType
#Bool

print(int(3.9))  #Python rounds towards zero not good for math if you rounding

#Null value is None
a = None
if a is None:
    print('Wepa')

b = bool(55)
if b is True:
    print('True')

if b is False:
    print('False')

if b is None:
    print('None')


c = 5
while c != 0:
    print(c)
    c -= 1

while True:
      response = input()
      if int(response) % 7 == 0:
         break


