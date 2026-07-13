# Sum of all odd numbers between 1 to n
def sum_odd(n):
    total = 0
    for i in range(1, n + 1, 2):
        if (i % 2 != 0):
            total += i
    return total

n = int(input("Enter value of n: "))
print("Sum of odd numbers from 1 to", n, "is:", sum_odd(n))
