# you are given all numbers between 1 and n except 1.
# first line contains n 

n = int(input())
lst = [int(x) for x in input().split()]

for i in range(1,n+1):
    if i in lst:
        None
    else:
        print(i)

