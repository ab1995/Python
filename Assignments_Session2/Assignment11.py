def readFile(*fileNames):
    for file in fileNames:
        for line in open(file,"r"):
            if line.count('')>30:
                print(line)

readFile('Assignment01.py')
