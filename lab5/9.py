# Write a Python program to insert spaces between words starting with capital letters.

import re

file = open("row.txt","r",encoding="utf8")
data = file.read()

stri = "HFDSKFhfskfJ jdffks JJJhfKk"
x = re.findall("[A-Z][a-z ]*",stri)

print(" ".join(x))    