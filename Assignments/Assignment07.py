matrixDimensions=input('Enter the Numbers: ')
tempDimensionsList=matrixDimensions.split(',')
X=int(tempDimensionsList[0])
Y=int(tempDimensionsList[1])
matrix= [[0 for y in range(Y)] for x in range(X)]

for x in range(X):
    for y in range(Y):
        matrix[x][y]=x*y

print(matrix)