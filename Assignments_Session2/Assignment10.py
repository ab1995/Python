import os

def findFiles(filePath):

    for dirname, dirnames, filenames in os.walk(filePath):

        for filename in filenames:
            if(filename.endswith('.py')):

                numOfLines = 0;
                for line in open(filename):
                    if line.strip():
                        if not line.startswith('#'):
                            numOfLines+=1

                print(os.path.join(dirname, filename), 'No. of Lines: ', numOfLines)

findFiles('C:')
#C:\Users\dhus_g\PycharmProjects