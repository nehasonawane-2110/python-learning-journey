# WAP to print the following pattern
# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1, 6):
    for j in range(1, i+1):  # print j inner loop form 1 to i+1 to print the number of stars in each row.
        print("*", end=" ")
    print()
