for number in range(1000,3000+1):
    digitList=[int(i) for i in str(number)]
    flag=1
    for digit in digitList:
        if digit%2!=0:
            flag=0
            break

    if flag==1:
        for digit in digitList:
            print(digit, end=',')
        print()

