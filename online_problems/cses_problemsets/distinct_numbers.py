#  5
#  2 3 4 2 2 returns 3


if __name__ == "__main__":
    n = int(input())
    count = 0
    lst = []

    for i in input().split():
        lst.append(i)
    
    print(len(set(lst)))

