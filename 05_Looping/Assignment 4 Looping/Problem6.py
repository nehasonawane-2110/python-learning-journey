# WAP to print sum of series upto n.

num = int(input("Enter the Number: "))
i = 1                 # Start from 1
sum_Of_series = 0     # Initialize sum to 0
while (i <= num):
# Loop runs from 1 to num
    sum_Of_series = sum_Of_series + i     # Add current value of i to sum
    i += 1
print("Sum of series =", sum_Of_series)
