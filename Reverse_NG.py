# Reverse Number guessing game, User picks a number and its the computers place to guess what it is.

from random import randint

def guess():
    low = 1
    high = 100
    x = ''  

    while x != 'c':
        g = randint(low, high)
        x = input(print(f'Is {g}, Your number (C), Too high (H) or Too low (L) ?')).lower()
        if x[0] == 'h':
            low = g + 1
        elif x[0] == 'l':
            high = g - 1
    print(f'Got your number! {g}')


guess()

