# we get a dna sequence: a string consisting of A,C,G,T  find the longest repetition in 
# the seq max lenght of one character return the number
#ATTCGGGA returns 3 for 3 gs

if __name__ == "__main__":
    seq = input()
    num = 1
    max = 1
    for i in range(0,len(seq)-1):
        if seq[i] == seq[i+1]:
            num += 1
            if num > max:
                max = num
        elif seq[i] != seq[i+1]:
            num = 1

    print(max)
    