def grams_to_ounces(grams):
    return grams*28.3495231
x=int(input())
print(grams_to_ounces(x))


def far_to_cel(Faren):
    Cel=(5/9)*(Faren-32)
    return Cel
x=int(input())
print(far_to_cel(x))


def solve(numheads, numlegs):
    rabbit=(numlegs-2*numheads)/2
    chicken=numheads-rabbit
    print("rabbit: ", int(rabbit), " chicken: ", int(chicken))
x=int(input())
y=int(input())
solve(x,y)


import math
def filter_prime(lst):
    primes = []
    for x in lst:
        if x < 2:
            continue
        is_prime = True
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
    return primes

n = int(input())
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)

print(filter_prime(numbers))


def permutation(word):
    if len(word) == 1:
        return [word]
    
    perms = permutation(word[1:])
    char = word[0]
    res = []

    for per in perms:
        for i in range(len(per)+1):
            res.append(per[:i] + char + per[i:])
    
    return res

wrd = input()
print(permutation(wrd))


def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

sentence = input()
print(reverse_sentence(sentence))


def three_33(arr):
    count = 0
    for i in range(len(arr)-1):
        if(arr[i] == arr[i+1] == 3):
            count+=1
        if count >= 1:
            return True
    return False

n = int(input())
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)

print(three_33(numbers))


def spy_game(arr):
    for i in range(len(arr)-2):
        if arr[i] == arr[i+1] == 0 and arr[i+2] == 7:
            return True
        else:
            continue
    return False


n = int(input())
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)

print(spy_game(numbers))


import math
def volume(R):
    print((4*math.pi*(R**3))/3)

radius = int(input())
volume(radius)



def unique_elems(arr):
    list = []
    for i in arr:
        if i not in list:
            list.append(i)
    return list

n = int(input())
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)

print(unique_elems(numbers))



def check(a):
    for i in range(len(a)//2):
        if a[i]!=a[-i-1]:
            return False
    return True

r = input()
print(check(r))


def his(arr):
    for i in range(len(arr)):
        print(arr[i]*'*')
    
his(list(map(int, input().split())))


import random
def guess():
    x = input("Hello! What is your name?")
    num = random.randint(1,20)
    print(f"Well, {x}, I am thinking of a number between 1 and 20.")
    i = 0
    while True:
        i+=1
        print("Take a guess.")
        popitka = int(input())
        if popitka == num:
            print(f"Good job, {x}! You guessed my number in {i} guesses!")
            break
        elif(popitka > num):
            print("Your guess is too big")
            continue
        elif(popitka < num):
            print("Your guess is too low")
            continue
        
guess()



def spy_game(arr):
    for i in range(len(arr)-2):
        if arr[i] == arr[i+1] == 0 and arr[i+2] == 7:
            return True
        else:
            continue
    return False

n = int(input())
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)

print(spy_game(numbers))

def solve(numheads, numlegs):
    rabbits = (numlegs - 2*numheads)/2
    chicken = numheads - rabbits
    print(int(rabbits), int(chicken))

inp = input()
x, y = map(int, inp.split())
solve(x, y)


