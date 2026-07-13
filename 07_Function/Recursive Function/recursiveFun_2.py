# Example 2 -
# Write a program to calculate the factorial using recursive function.

def fact(n):
    if (n == 0):
        return 1       # Return 1 because factorial of 0 is 1
    else:
        return n * fact(n-1)     # Recursive call: multiply n with factorial of (n-1)


n = int(input("enter the number: "))
sum = fact(n)
print(sum)