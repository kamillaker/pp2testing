# Write a Python program to convert degree to radian.
from math import radians
print(radians(int(input())))

#Write a Python program to calculate the area of a trapezoid.
#Height: 5
#Base, first value: 5
#Base, second value: 6
#Expected Output: 27.5

def area_trapezoid(h,a,b):
    print(h*(1/2)*(a+b)) 

area_trapezoid(float(input("Height: ")),float(input("Base, first value: ")),float(input("Base, second value: ")))

# Write a Python program to calculate the area of regular polygon.
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625

from math import *
def area_reg_polygon(sides,len):
    print(sides/4*len**2*(1/(tan(radians(180/sides)))))

sides = float(input("Input number of sides: "))
length = float(input("Input the length of a side: "))
print("The area of the polygon is: ")
area_reg_polygon(sides,length)

#Write a Python program to calculate the area of a parallelogram.
#Length of base: 5
#Height of parallelogram: 6
#Expected Output: 30.0

def area_parallelogram(len,h):
    print(len*h)

length = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))
area_parallelogram(length,h)



