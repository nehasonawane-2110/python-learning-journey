# write a program to print the even unmber form 1 to N

n = int(input("Enter the number: "))
i = 1
while (i <= n):
    if (i % 2 == 0):  # Check if the number is even
        print(i)
    i += 1
