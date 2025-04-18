import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.match(string))

def isValidNumber(string: str):
    valid = False
    try:
        float(string)
            valid = True
        except ValueError:
        return valid

def isEmpty(string: str):
    return len(string) == 0