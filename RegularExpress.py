import re

string = "idfjgdgdfkdfj"

digit = re.search(r'\d+', string)
print(digit.group())
