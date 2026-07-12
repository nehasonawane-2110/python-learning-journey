# WAP to check if a given number is prime number or not.

num = int(input("Enter a number: "))
for i in range(2, num): 
    if (num % i == 0):
        print(f'{num} is not a prime number.')
        break    # break is used to exit the loop if the condition is true.
else:
    print(f'{num} is a prime number.')
