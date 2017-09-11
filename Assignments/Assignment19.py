from operator import itemgetter

l = []
while True:
    item = input('Enter Elements:')
    if not item:
        break
    l.append(tuple(item.split(",")))

print(sorted(l, key=itemgetter(0, 1, 2)))
