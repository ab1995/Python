class StringOperations():
    string=''

    def getString(self):
        self.string=input('Enter the String: ')

    def printString(self):
        print(self.string)

stringObj=StringOperations()
stringObj.getString()
stringObj.printString()