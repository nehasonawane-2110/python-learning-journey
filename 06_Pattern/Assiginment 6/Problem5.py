# Write a program to print the following pattern 
#         1
#       1 2 3
#     1 2 3 4 5
#   1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8 9

for i in range(1, 6):

    # spaces
    for j in range(1, 6 - i):  # decrementing the number of space by 1(4, 3, 2, 1, 0)
        print(" ", end=" ")

    # numbers
    for j in range(1, 2 * i):   # incrementing the number of element in each row by 2 (1, 3, 5, 7, 9)
        print(j, end=" ")

    print()
