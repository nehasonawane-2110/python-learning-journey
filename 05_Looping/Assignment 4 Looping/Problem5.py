# WAP to print the all odd number until n.
num = int(input("Enter the Number: "))
i = 0
while (i <= num):
    if (i % 2 != 0):   # Check if number is odd (remainder not equal to 0)
        print(i)
    i += 1
