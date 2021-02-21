from random import randint
 
def roll():
    num = randint(1,6)
    if num == 1:
        print('+ - - - - +')
        print('|         |')
        print('|    o    |')
        print('|         |')
        print('+ - - - - +')
    elif num == 2:
        print('+ - - - - +')
        print('| o       |')
        print('|         |')
        print('|       o |')
        print('+ - - - - +')
    elif num == 3:
        print('+ - - - - +')
        print('| o       |')
        print('|    o    |')
        print('|       o |')
        print('+ - - - - +')
    elif num == 4:
        print('+ - - - - +')
        print('| o     o |')
        print('|         |')
        print('| o     o |')
        print('+ - - - - +')
    elif num == 5:
        print('+ - - - - +')
        print('| o     o |')
        print('|    o    |')
        print('| o     o |')
        print('+ - - - - +')
    elif num == 6:
        print('+ - - - - +')
        print('| o  o  o |')
        print('|         |')
        print('| o  o  o |')
        print('+ - - - - +')


if __name__ == "__main__":
    roll()
