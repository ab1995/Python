contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

for line in contents:
    print(line.upper())