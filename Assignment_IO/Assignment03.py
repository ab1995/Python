import re

def avoids():
    forbiddenLetters='['+input('Enter Forbidden Letters: ')+']'
    wordToVerify=input('Enter the Word: ')

    if not re.search(forbiddenLetters,wordToVerify):
        print(wordToVerify)

avoids()
