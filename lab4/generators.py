# 1 Create a generator that generates the squares of numbers up to some number N.

def squares(start , end):
    while start <= end :
        yield str(start**2)
        start +=1

print(", ".join(list(squares(int(input()),int(input())))))

# 2 Write a program using generator to print the even numbers between 0 and n
# in comma separated form where n is input from console.

def evens(n):
    for i in range(n+1):
        if i % 2 == 0 :
            yield i 

print(", ".join(list(map(str, evens(int(input()))))))

# 3 Define a function with a generator which can iterate the numbers,
# which are divisible by 3 and 4, between a given range 0 and n.

def div_3_4(n):
    for i in range(n+1):
        if i % 3 == 0  and i % 4 == 0 :
            yield i

print(", ".join(list(map(str,div_3_4(int(input()))))))

# 4 Implement a generator called squares to yield the square of all numbers from (a) to (b).
# Test it with a "for" loop and print each of the yielded values.

def squares(a,b):
    while a<=b:
        yield a**2
        a += 1

a , b = int(input()) , int(input())
iter = squares(a,b)
for i in range (a,b+1) :
    print(next(iter),end=" ")


# 5 Implement a generator that returns all numbers from (n) down to 0.

def int_n_0(n):
    while n>=0:
        yield n
        n -= 1 

iter = int_n_0(int(input()))
for i in iter:
    print(i,end=" ")