# Reverse Number guessing game, User picks a number and its the computers place to guess what it is.

from random import randint
import time

def guess():
    print('Hello! Please pick a number between 0 and 100, I will try and guess it :) Are you ready?')
    low = 1
    high = 100
    x = ''
    #time.sleep(2)
   
    while x[0] != 'x':
        g = randint(low,high)
        x = input(print(f'Is {g}, Your number (C), Too high (H) or Too low (L) ?')).lower()
        if x[0] == 'h':
            low = g + 1
        elif x[0] == 'l':
            high = g - 1

    print(f'Got your number! {g}')


guess()

