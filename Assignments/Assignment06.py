commaSeparatedNumbers=input('Enter the Numbers: ')
numberList=commaSeparatedNumbers.split(',')

C, H=50, 30
for number in numberList:
    print(int((2*C*int(number))/H), end=',')