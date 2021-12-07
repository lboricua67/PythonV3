#!/usr/bin/env python3

from Person import Person

class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        self.pay *= (1.0 + percent + bonus)
        return self.pay

