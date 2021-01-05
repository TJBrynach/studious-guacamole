# you are given all numbers between 1 and n except 1.
# first line contains n 
    

if __name__ == "__main__":
    n = int(input())
    total = n * ( n + 1 ) / 2
    sum = 0

    for x in input().split():
        sum += int(x)

    missing_number = int(total) - sum
    print(missing_number)

#