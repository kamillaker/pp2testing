# 5 Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

file = open("row.txt","r",encoding="utf8")
data = file.read()
x = re.search("a.*b",data)
print(x.group())