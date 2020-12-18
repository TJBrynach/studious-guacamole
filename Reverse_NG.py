# Reverse Number guessing game, User picks a number and its the computers place to guess what it is.

from random import randint
import time

def guess():
    print('Hello! Please pick a number between 0 and 100, I will try and guess it :) Are you ready?')
    low = 1
    high = 100
    g = randint(low,high)
    time.sleep(3)
    x = input(print(f'Is {g}, Your number (C), Too high (H) or Too low (T) ?'))
    
    while x != 'C' or x != 'c':

"""

    while x[0] == 'n' or x[0] == 'N':
        hol = input(print('higher or lower : '))
        if hol[0] == 'h' or hol[0] == 'H':
            low = g
            g1 = randint(low,high)
            y = input(print(f'Is your number : {g1}  ?'))
        else:
            g1 = randint(low,high)
            high = g
            y = input(print(f'Is your number : {g1}  ?'))
"""


guess()

