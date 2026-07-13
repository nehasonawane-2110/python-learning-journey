# Menu Driven Program
# ===================== MENU DRIVEN PROGRAM =====================

# 1. Even Odd - checks whether number is even or odd
# Example: Input: 4 → Output: Even Number
def evenOdd(num):
    if num == 0:
        return f'{num} is Neutral.'
    elif num % 2 == 0:
        return f'{num} is an Even Number.'
    else:
        return f'{num} is an Odd Number.'


# 2. Positive Negative - checks sign of number
# Example: Input: -5 → Output: Negative Number
def CheckPositiveNegative(num):
    if num > 0:
        return f"{num} is Positive Number."
    elif num < 0:
        return f"{num} is Negative Number."
    else:
        return f"{num} is Zero"


# 3. Prime Number - number divisible only by 1 and itself
# Example: Input: 7 → Output: Prime Number
def checkPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # check till √num (optimized)
        if num % i == 0:
            return False
    return True


# 4. Palindrome Number - same forward and backward
# Example: Input: 121 → Output: Palindrome
def palindromeNumber(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit   # building reverse number
        num = num // 10

    if original == reverse:
        return f"{original} is a Palindrome Number."
    else:
        return f"{original} is not a Palindrome Number."


# 5. Perfect Number - sum of divisors = number
# Example: Input: 6 → Output: Perfect (1+2+3=6)
def PerfectNumber(num):
    sum_of_divisors = 0
    for i in range(1, num):   # checking proper divisors
        if num % i == 0:
            sum_of_divisors += i

    if sum_of_divisors == num:
        return f'{num} is a Perfect Number.'
    else:
        return f'{num} is not a Perfect Number.'


# 6. Strong Number - sum of factorial of digits = number
# Example: Input: 145 → Output: Strong (1!+4!+5!=145)
def strongNumber(num):
    temp = num
    sum_of_digit = 0

    while temp > 0:
        digit = temp % 10
        temp = temp // 10

        fact = 1
        for i in range(1, digit + 1):   # factorial of each digit
            fact *= i

        sum_of_digit += fact

    if sum_of_digit == num:
        return f'{num} is a Strong Number.'
    else:
        return f'{num} is not a Strong Number.'


# 7. Armstrong Number - sum of digits^power = number
# Example: Input: 153 → Output: Armstrong
def ArmstrongNumber(num):
    temp = num
    count = 0  # count digits

    while (temp > 0):    # counting digits
        temp = temp // 10
        count += 1

    temp = num
    sum_of_digits = 0
    while temp > 0:        # calculating sum of digits raised to power of count
        digit = temp % 10
        sum_of_digits += digit ** count   # digit raised to power of count
        temp = temp // 10

    if (sum_of_digits == num):
        return f'{num} is an Armstrong Number.'
    else:
        return f'{num} is not an Armstrong Number.'


# 8. Fibonacci Series - sum of previous two numbers
# Example: n=5 → Output: 0 1 1 2 3
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        temp = a + b   # next number
        a = b
        b = temp


# 9. Sum of Digits - add all digits of number
# Example: Input: 123 → Output: 6
def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
    return total


# 10. Reverse Number - reverse digits
# Example: Input: 123 → Output: 321
def reverse_number(num):
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit   # shifting digits
        num = num // 10
    return reverse


# ===================== MENU =====================
ch = 0

while (ch != 11):

    print('''
1. Even Odd
2. Positive Negative
3. Prime Number
4. Palindrome Number
5. Perfect Number
6. Strong Number
7. Armstrong Number
8. Fibonacci Series
9. Sum of Digits
10. Reverse Number
11. Exit
''')

    ch = int(input("Enter Choice: "))

    if ch == 1:
        num = int(input("Enter number: "))
        print(evenOdd(num))

    elif ch == 2:
        num = int(input("Enter number: "))
        print(CheckPositiveNegative(num))

    elif ch == 3:
        num = int(input("Enter number: "))
        if checkPrime(num):
            print(f"{num} is a Prime Number.")
        else:
            print(f"{num} is not a Prime Number.")

    elif ch == 4:
        num = int(input("Enter number: "))
        print(palindromeNumber(num))

    elif ch == 5:
        num = int(input("Enter number: "))
        print(PerfectNumber(num))

    elif ch == 6:
        num = int(input("Enter number: "))
        print(strongNumber(num))

    elif ch == 7:
        num = int(input("Enter number: "))
        print(ArmstrongNumber(num))

    elif ch == 8:
        n = int(input("Enter number of terms: "))
        print("Fibonacci Series:", fibonacci(n))

    elif ch == 9:
        num = int(input("Enter number: "))
        print("Sum of digits:", sum_of_digits(num))

    elif ch == 10:
        num = int(input("Enter number: "))
        print("Reverse number:", reverse_number(num))

    elif ch == 11:
        print("Thank You!")

    else:
        print("Invalid Choice...")