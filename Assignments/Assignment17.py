contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

accountBalance=0

for line in contents:
    lineSplit=line.split()
    print(lineSplit[0])
    if(lineSplit[0]=='D'):
        accountBalance+=int(lineSplit[1])
    if(lineSplit[0]=='W'):
        accountBalance-=int(lineSplit[1])

print("Account Balance: ", accountBalance)

