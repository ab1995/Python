import re

forbiddenLetters='['+input('Enter Forbidden Letters: ')+']'
wordCount=0
for line in open('words.txt'):
    for word in line.split():
        if not re.search(forbiddenLetters, word):
            wordCount+=1

print('Word Count: ',wordCount)