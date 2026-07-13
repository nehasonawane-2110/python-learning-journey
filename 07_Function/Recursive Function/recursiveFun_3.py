# Example 3-
# Write a program to calculate the fibbonacci series using recurive function

def fibbo(n, a, b):        # Function definition with three parameters
    # n = number of terms to print
    # a = first previous number
    # b = second previous number

    if (n > 0):          # Condition to continue recursion until n becomes 0
        c = a + b
        print(c)
        fibbo(n - 1, b, c)     # Recursive call
    # n-1 decreases the count
    # b becomes next previous number
    # c becomes current number


num = int(input("Enter the number: "))
a = -1    # Initialize first value
b = 1     # Initialize second value
fibbo(num, a, b)
