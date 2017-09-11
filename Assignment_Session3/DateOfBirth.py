from datetime import date
day=int(input('Enter day of DOB: '))
month=int(input('Enter month of DOB: '))
year=int(input('Enter year of DOB: '))
dob=date(year, month, day)
print(date.today()-dob)