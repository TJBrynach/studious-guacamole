import random
from nltk.corpus import words


# Generating the random word
def rand_word():
    wordlst = words.words()
    rand_word = random.choice(wordlst).lower()
    return rand_word

WORD = rand_word()
letters = []
g_word = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def set_up() -> None:
    """setting up the game and selecting the word for the game"""
    print('Hello, welcome to Hangman!\n')

    for char in WORD:
        g_word.append('-')
    print(' '.join(g_word))
    print('Ok, the word you need to guess has, ', len(WORD), 'characters')


def guessing():
    moves = 0
    while moves < 10:
        move = str(input('guess a letter : ')).lower()
        if len(move) > 1:
            print('One letter at a time please')
        elif move not in alphabet:
            print('A letter please, from a to z')
        elif move in letters:
            print('Already guessed that letter, try another')
        else:
            letters.append(move)
            if move in WORD:
                print('Nice one bud, you found one!')
                for i in range(0, len(WORD)):
                    if WORD[i] == move:
                        g_word[i] = move
                moves += 1
                print(" ".join(g_word))
                print('You have', 10 - moves,' moves remaining!')
                print('Used letters are: '," ".join(letters))
                if '-' not in g_word:
                    print('You have won, Congratz!')
                    break
            else:
                print('That letter is not in the word')
                moves +=1
                print(" ".join(g_word))
                print('You have', 10 - moves,' moves remaining!')
                print('Used letters are: '," ".join(letters))

                if moves == 10:
                    print(f'Game over better luck next time, the word was {WORD}')




                




if __name__ == "__main__":
    set_up()
    guessing()