# elif ladder
# even odd number (zero) check using elif ladder.

num = int(input("Enter the number:"))

if (num == 0):
    print(f'{num} is neutral number.')
elif (num % 2 == 0):      # check the remainder is exact equal to zero or not(==)
    print(f'{num} is even number.')
else:
    print(f'{num} is odd number.')
