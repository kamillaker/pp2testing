# 2 Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

file = open("row.txt","r",encoding="utf8")
data = file.read()
x = re.search("ab{2,3}",data)
print(x.group())