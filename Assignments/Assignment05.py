class StringManipulator():
    stringMessage=""

    def __init__(self, stringMessage):
        self.stringMessage=stringMessage

    def setString(self):
        self.stringMessage=input('Enter the string message: ')

    def printString(self):
        print(self.stringMessage.upper())

obj=StringManipulator("Python is Great!")
obj.printString()