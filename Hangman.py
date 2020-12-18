import random
from nltk.corpus import words

def hangman():
    guessed_letters = []
    moves = 0
    

    # Generating the random word
    wordlst = words.words()
    rand_word = random.choice(wordlst).lower()
    print(rand_word)
    
    
    move  = str(input('guess a letter : ')).lower()

    while moves < 6:
        if len(move) > 1:
            print('One letter at a time please')
        elif move in guessed_letters:
            print('Already guessed that letter, try another')
        else:
            guessed_letters.append('move')
            i = 0
            while i < len(word):
                if move == word[i]:
                    new_blankslist[i] = guessed_letters[i]
                i = i + 1
            if new_blanks_list





hangman()