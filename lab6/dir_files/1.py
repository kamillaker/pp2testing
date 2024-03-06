# Write a Python program to list only directories, files and all directories, files in a specified path.

import os

folder_name = input()
path = f"../{folder_name}/"

dirs_list = os.listdir(path)

print("directories:")
for dir in dirs_list:
    if os.path.isdir(dir):
        print(dir)
        
print("files:")
for dir in dirs_list:
    if os.path.isfile(dir):
        print(dir)


# Write a Python program to check for access to a specified path. 
# Test the existence, readability, writability and executability of the specified path

import os

path = os.getcwd()

print(f"Existence: {os.access(path,os.F_OK)}")
print(f"Readability: {os.access(path,os.R_OK)}")
print(f"Writability: {os.access(path,os.W_OK)}")
print(f"Executability: {os.access(path,os.X_OK)}")

# Write a Python program to test whether a given path exists or not.
# If the path exist find the filename and directory portion of the given path.

import os

path = os.getcwd()

if os.access(path , os.F_OK):
    print(os.listdir(path))

# Write a Python program to count the number of lines in a text file.

with open("text.txt", "r") as file:
    s = sum(1 for line in file)

print(s)


# Write a Python program to write a list to a file.

list = input().split()

with open ("text.txt", "w") as file:
    file.write(" ".join(list))



# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

for i in range(26):
    with open(f"{chr(i+65)}.txt",'x') as file:
        pass


# Write a Python program to copy the contents of a file to another file

with open("text.txt","r") as file:
    content = file.read()
    
with open("f2.txt","w") as file2:
    file2.write(content)





# Write a Python program to delete file by specified path. 
# Before deleting check for access and whether a given path exists or not.

import os
path = "del"
if os.access(path,os.F_OK):
    os.rmdir(path)