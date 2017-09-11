class ReverseItr:
    def __init__(self, a, b):
        self.a = a
        self.b = b + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.b <= self.a:
            raise StopIteration
        else:
            self.b -= 1
            return self.b


rev = ReverseItr(1, 60)
for x in rev:
    print(x)

#comment