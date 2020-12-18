### First Edition
from random import randint


def number_guesser():
    print("Welcome to the number guesser game! Would you like to play?")
    x = input()
    if x[0] == 'y' or x[0] == 'Y':
        print("Lets get this show on the road, number is being generated between 0-100, you have 5 guesses to get this correct")
        
        num = randint(1,100)
        guess = int(input("Our number to guess has been randomly generated. Guess a number between 1 and 100 :  "))
        guess_count = 0
        
        while guess_count <= 6:
            if guess == num:
                print(f'Well done, you got it!, you have correctly guessed {num}!!!')
                break

            elif guess > num:
                print("Sorry try again. Your guess was too high")
                guess_count += 1
                guess = int(input("What is your next guess :  "))

            elif guess < num:
                print("Sorry try again, your guess was too low")
                guess_count += 1
                guess = int(input("What is your next guess :  "))
    else:
        print("Ah well maybe another time")

number_guesser()