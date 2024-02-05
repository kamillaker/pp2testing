class MyClass:   
    def getString(self):
        self.a=str(input())
    
    def printString(self):
        print(self.a.upper())

p1=MyClass()
p1.getString()
p1.printString()


class Shape:
    def area(self):
        print(0)
class Square(Shape):
        def __init__(self, length):
            self.length=length
        
        def area(self):
            print(self.length*self.length) 

x=Square(int(input()))
y=Shape()
x.area()
y.area()



class Shape:
    def area(self):
        print(0)
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area(self):
        print(self.length*self.width)

x=Rectangle(int(input()), int(input()))
y=Shape()
x.area()
y.area()


import math
class Point:
    def __init__(self, x1, y1):
        self.x1=x1
        self.y1=y1
    def show(self):
        print("Coordinates: ", self.x1, self.y1) 
    def move(self, x2, y2):
        self.x2=x2
        self.y2=y2
        print("Next coordinates:",self.x2, self.y2)
    def dist(self):
        print("Distance between two points:",math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2))

x=Point(int(input()), int(input()))
x.show()
x.move(int(input()), int(input()))
x.dist()




class Account:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def deposit(self, months, percent):
        for i in range(months):
            self.balance+=self.balance*(percent/100)
        print("Your current balance is equal to", self.balance)
    def withdraw(self, wtdr):
        if wtdr<0:
            print("You haven't withdrawn the money")
        elif wtdr>self.balance:
            print("Your balance does not have such a withdraw")
        else:
            print("You took it off", wtdr, " and your current balance is exactly ", self.balance-wtdr)
            self.balance=self.balance-wtdr
x=Account("Alina", 50000)
x.deposit(24, 15)
x.withdraw(25000)




lst = list(map(int, input().split()))
primes = filter(lambda x: all(x%i != 0 for i in range(2, x)), lst)
result = list(primes)
if 1 in result:
    result.remove(1)
print(result)