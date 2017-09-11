sentence=input("Enter the Sentence: ")

charCount=0
digitCount=0

for char in sentence:
    if char.isdigit():
        digitCount+=1
    if char.isalpha():
        charCount+=1

print("Characters: ",charCount)
print("Digits: ", digitCount)