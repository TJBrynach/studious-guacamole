# A permutation of integers is called beautiful if there are no adj 
# elements whos difference is 1, taking in one integer 
#

if __name__ == "__main__":
    n = int(input())

    if n == 1:
        print(1)
    elif 2 <= n <= 3:
        print('NO SOLUTION')
    else:
        lst = [*range(2, n + 1, 2), *range(1, n + 1, 2)]
        print(' '.join(map(str, lst)))



# 2 4 1 3

    
            
