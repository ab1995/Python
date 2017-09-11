import re

passwdList=[x for x in input('Password To Verify: ').split(',')]
for passwd in passwdList:
    if len(passwd)<6 or len(passwd)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",passwd):
        continue
    elif not re.search("[0-9]",passwd):
        continue
    elif not re.search("[A-Z]",passwd):
        continue
    elif not re.search("[$#@]",passwd):
        continue
    elif re.search("\s",passwd):
        continue
    else:
        pass
    print(passwd, end=',')
