# 7 Write a python program to convert snake case string to camel case string.

import re 

file = open("row.txt", "r" ,encoding= "utf8")
data = file.read()

x = re.findall("_[a-z]",data)

for y in x :
    data = re.sub(y,y[1].upper(),data)
print(data)