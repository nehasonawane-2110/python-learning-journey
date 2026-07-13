# 5. Sum of all prime numbers between 1 to n

# Function to check if a number is prime
def check_prime(num):
    if num < 2:                       # 0 and 1 are not prime
        return False
 
    for i in range(2, num // 2 + 1):  # check divisibility
        if num % i == 0:
            return False              # not prime

    return True                       # prime


# Function to find sum of prime numbers from 1 to n
def sum_of_primes(n):
    total = 0                         # initialize sum

    for i in range(1, n + 1):         # loop from 1 to n
        if check_prime(i):            # check if number is prime
            total += i                # add to sum

    return total                      # return final sum


# Main program
n = int(input("Enter the Number: "))
print("Sum of all prime numbers between 1 to", n, "is:", sum_of_primes(n))
