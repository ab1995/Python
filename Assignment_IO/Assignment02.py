import re
def has_no_e():
    wordWithoutE=0
    totalWords=0

    for line in open('words.txt'):
        for word in line.split(' '):
            if not re.search("[e]", word):
                print(word)
                wordWithoutE+=1
            totalWords+=1

    print('Percentage of words without E: ',100-(wordWithoutE/totalWords*100))

has_no_e()