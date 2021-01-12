#array of n integers
# On each move, you may increase the value of any element by one. 
# What is the minimum number of moves required?
# 3 2 5 1 7 

if __name__ == "__main__":
    n = int(input())
    count = 0
    lst = input().split()

    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j] >= lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                count += 1
        
    print(count)