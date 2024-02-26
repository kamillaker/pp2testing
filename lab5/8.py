# 8 Write a Python program to split a string at uppercase letters.

import re 

file = open("row.txt", "r" ,encoding= "utf8")
data = file.read()

l = re.split("[A-Z]" ,data)
print(l)