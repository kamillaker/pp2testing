# 3 Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

file = open("row.txt","r",encoding="utf8")
data = file.read()
x = re.findall("[a-z]_[a-z]",data)
print(x)