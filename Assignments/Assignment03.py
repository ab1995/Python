number=(int(input('Enter the Number: ')))
squareMap={}
for num in range(1, number+1):
    squareMap[num]=num**2

print(squareMap)