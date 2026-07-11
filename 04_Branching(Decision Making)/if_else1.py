# number is even or odd its check.  (if-else condition statement)

num = int(input("Enter the number: "))

if (num % 2 == 0):     # remainder check is exact equal to zero or not(==)
    print(f'{num} is the even number.')
else:
    print(f'{num} is the odd number.')
