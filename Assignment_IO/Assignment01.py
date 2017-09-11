import re

def has_no_e(wordToCheck):
    if not re.search("[e]", wordToCheck):
        return True

print(has_no_e("word"))