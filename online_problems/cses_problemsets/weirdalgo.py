### algo that takes as an input a positive integer n.
# if n is even divide by 2
# if n is odd multiply by 3 and add 1. until n is one
#

def algo(n):
    if n % 2 == 0:
        n  = n / 2
        return n
    elif n % 2 == 1:
        n = (n * 3) + 1
        return n

a=int(input())
l = [a]
while (a != 1):
    a = int(algo(a))
    l.append(a)

for i in range(len(l)):
    print(l[i], end=' ')
