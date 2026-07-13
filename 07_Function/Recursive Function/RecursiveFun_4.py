# Example 4 -
# Write a program to calculate the sum of digit using the recursive function.

def sumOfDigit(n):
    if (n == 0):
        return 0
    else:
        return (n % 10) + sumOfDigit(n // 10)
        # n % 10 gives the last digit
        # n // 10 removes the last digit
        # Recursive call to process remaining digits


n = int(input("Enter the number: "))
res = sumOfDigit(n)
print(res)
