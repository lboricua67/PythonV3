#!/usr/bin/env python3

from Person import Person

Y=Person
Y.name="Ramon Santiago"
Y.age=45
Y.pay=2500

X=Person.lastname(Y)
R="${:,.2f}".format(Person.giveraise(Y,2))
print(X)
print(R)
