x = iter([1,2,3])

def peep(x):
    return([x.__next__(), x ])
print(peep(x))