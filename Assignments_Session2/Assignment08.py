import os


def findFiles(filePath):
    pythonFilesCount = 0
    for dirname, dirnames, filenames in os.walk(filePath):


        for filename in filenames:
            if(filename.endswith('.py')):
                pythonFilesCount=pythonFilesCount+1

    return  pythonFilesCount

pythonFilesCount=0
print(findFiles('D:'))