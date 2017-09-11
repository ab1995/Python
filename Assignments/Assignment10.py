spaceSeparatedString=input('Enter the String: ')
stringList=spaceSeparatedString.split()
stringSet=set()

for string in stringList:
    stringSet.add(string)

stringList=(list(stringSet))
stringList.sort()
print(stringList)
