# 4 Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

str = 'iasndRinRssdnjnn'
x = re.findall('[A-Z][a-z]+', str)
print(x)