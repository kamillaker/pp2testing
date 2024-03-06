# Write a Python program with builtin function to multiply all the numbers in a list

import math

list = [int(x) for x in input().split()]

print(math.prod(list))


# Write a Python program with builtin function that accepts a string
# and calculate the number of upper case letters and lower case letters

def num_of_letterS(dtring):
    up = sum(1 for let in string if let.isupper())
    low = sum(1 for let in string if let.islower())
    return up , low

string = input()
up , low = num_of_letterS(string)
print(f"number of upper letters {up}")
print(f"number of lower letters {low}")


# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def is_pal(string):
    rev_str = "".join(reversed(string))
    return rev_str == string

string = input()
if is_pal(string) :
    print(f"{string} is palindrome" )
else:
    print(f"{string} is not palindrome")



# Write a Python program that invoke square root function after specific milliseconds.

from time import sleep
from math import sqrt

num = int(input())
millisecond = int(input())

sleep(millisecond/1000)

print(f"Square root of {num} after {millisecond} miliseconds is {sqrt(num)}")


# Write a Python program with builtin function that returns True if all elements of the tuple are true.

mytuple = (True, True , True, True )

print(all(mytuple))