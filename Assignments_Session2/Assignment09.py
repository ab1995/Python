import os

def findFiles(filePath):

    for dirname, dirnames, filenames in os.walk(filePath):

        for filename in filenames:
            if(filename.endswith('.py')):
                numOfLines = sum(1 for line in open(filename))
                print(os.path.join(dirname, filename), 'No. of Lines: ', numOfLines)

findFiles('C:')