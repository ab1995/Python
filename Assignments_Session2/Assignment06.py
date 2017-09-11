import datetime
from datetime import date

class Person:

    def __init__(self):
        self.birthDate = date(1995 ,5, 23)
        today = date.today()
        self.age = today.year - self.birthDate.year - ((today.month, today.day) < (self.birthDate.month, self.birthDate.day))

    def getAge(self):
        return self.age

    def calculateAge(self):
        today = date.today()
        return today.year - self.birthDate.year - ((today.month, today.day) < (self.birthDate.month, self.birthDate.day))

x = Person()
print(x.getAge())
print(x.calculateAge())