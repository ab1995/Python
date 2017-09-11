import re

def uses_only(allowedLetters, wordToVerify):
    if  re.search(allowedLetters, wordToVerify):
        return True

allowedLetters='['+input('Enter Allowed Letters: ')+']'
wordToVerify=input('Enter the Word: ')
print(uses_only(allowedLetters, wordToVerify))