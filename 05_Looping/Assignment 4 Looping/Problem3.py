# WAP to print first n prime numbers

n = int(input("Enter a number: "))
count = 0  # This variable counts how many prime numbers we have printed so far.
num = 2    # Start checking from number 2 because 2 is the first prime number.

while (count < n):
    for i in range(2, num // 2 + 1):
        # Check divisibility from 2 to num//2.
        # If a number has a factor, it must be less than or equal to num//2.
        if (num % i == 0):
            # If num is divisible by i,
            # then num is NOT a prime number.
            break
    else:
        print(num)
        count += 1
    num += 1
