# 6 Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

file = open("row.txt", "r", encoding = "utf8")
data = file.read()

x = re.sub("[ ]|[,]|[.]",":", data)

print(x)