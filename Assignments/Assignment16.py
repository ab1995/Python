commaSeparatedIntegers=input('Enter the Binary Numbers: ')
numberList=commaSeparatedIntegers.split(',')

for number in numberList:
    if int(number)%2!=0:
        print(number,end=',')