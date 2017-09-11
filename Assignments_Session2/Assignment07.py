import os

def findFiles(filePath):

    for dirname, dirnames, filenames in os.walk('.'):

        for subdirname in dirnames:
            print(os.path.join(dirname, subdirname))

        for filename in filenames:
            print(os.path.join(dirname, filename))


findFiles('D:\Softwares_for_freshers_training')