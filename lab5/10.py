# Write a Python program to convert a given camel case string to snake case.

import re 

file = open("row.txt", "r" ,encoding= "utf8")
data = file.read()

x = re.findall("[A-Z]",data)

for y in x :
    data = re.sub(y,"_"+y.lower(),data)
print(data)