sentence=input("Enter the Sentence: ")

lowerCaseCount=0
upperCaseCount=0

for char in sentence:
    if char.isupper():
        upperCaseCount+=1
    if char.islower():
        lowerCaseCount+=1

print("Upper Case Count: ",upperCaseCount)
print("Lower Case Count: ", lowerCaseCount)