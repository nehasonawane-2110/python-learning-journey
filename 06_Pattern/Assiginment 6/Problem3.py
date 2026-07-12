# parcal triangle

for i in range(0, 4):   # num of rows
    for j in range(0, 3 - i):    # spaces
        print(" ", end=" ")
    num = 1             # first number of every row is 1
    for j in range(0, i + 1):    # incrementing the number of element in each row
        print(num, end="  ")
        num = num * (i - j)//(j + 1)    # formula to calculate the next number in the same row
    print()
