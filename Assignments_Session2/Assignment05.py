class Rectangle:
    def __init__(self,length,breadth):
        self.length =length
        self.breadth =breadth

    def calculateArea(self):
        return self.length*self.breadth


rect = Rectangle(4,5)
print (rect.calculateArea())