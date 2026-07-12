# Problem 1
# Write a program to print the following pattern:
# Hollowgram pattern
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

for i in range(1, 6):
    for j in range(1, 6, 1):
        if (j == 1 or j == 5 or i == 1 or i == 5):
            print('*', end=" ")
        else:
            print(' ', end=" ")
    print()
