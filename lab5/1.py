# 1 Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

data1 = "abbbbbdhfhdfkld"
file = open("row.txt","r",encoding="utf8")
data = file.read()
x = re.search("ab*",data1)
print(x.group())