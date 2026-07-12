# Defination : A pattern is repeated or regular arrangement of number, symbol, letter or shape that folloe the specific rule or design.
# Pattern 1.
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

for i in range(1, 6):   # outer loop for rows
    for j in range(1, 6):   # Inner loop for colums
        print("*", end=" ")
    print()   # print a new line after each row is printed
