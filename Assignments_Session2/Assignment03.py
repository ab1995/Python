class Generator:
    def __init__(self,endLimit):
        self.endLimit=endLimit

    def nextVal(self):
        a=0
        while a<self.endLimit:
            if a%7==0:
                temp =a
                a+=1
                yield temp
            else:
                a+=1

x= Generator(100)
y=x.nextVal()
print(next(y))
print(next(y))
print(next(y))
print(next(y))
