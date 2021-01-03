# Given the names and grades for each student in a calss of N students,
# store them in a nested list and print names of any students having the
# second lowest grade. If multiple are second lowest print in alphabetical
# order
# records = [["chi", 20.0],["beta",10.0],["alpha",50.0]

# Initialising the two lists
lst = []
marks_lst = []

n = int(input())

for i in range(n):
    name = input()
    mark = float(input())
    record = [name, mark]
    lst.append(record)
    marks_lst.append(mark)

lst.sort()


second_lowest = sorted(set(marks_lst))[1]

for i, j  in lst:
    if j == second_lowest:
        print(i)
