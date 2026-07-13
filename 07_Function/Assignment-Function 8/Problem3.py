# 3). Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def factorial(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact


def sum_factorial(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total


def sum_power(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total


# Main
n = int(input("Enter value of n: "))

print("Sum of 1 + 2 + ... + n =", sum_n(n))
print("Sum of 1! + 2! + ... + n! =", sum_factorial(n))
print("Sum of 1^1 + 2^2 + ... + n^n =", sum_power(n))