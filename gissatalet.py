import random
n = random.randint(1, 10)


guess = 0
try:
    guess = int(input("skriv ett tal mellan 1 och 10: "))
except: 
    pass

import sys


while n != "guess": 
    while guess == 0:
        try:
            guess = int(input("skriv ett tal mellan 1 och 10: "))
        except: 
            print ("du MÅSTE SKRIVA BOKSTÄVER NOOB -_-")

    print
    if guess < n:
        print("gissningen är för låg")
        guess = int(input("skriv ett tal mellan 1 och 10: "))
    elif guess > n:
        print("gissningen är för hög")
        guess = int(input("skriv ett tal mellan 1 och 10: "))
    else:
        print ("du gissade rätt!") 
        print ("kill")
        break


