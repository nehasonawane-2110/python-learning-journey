# WAP to check if given number is Perfect Number.

num = int(input("Enter Number: "))
i = 1
sum_of_divisors = 0    # 1 + 2 + 3 = 6 (perfect number)
while (i < num):
    if (num % i == 0):
        sum_of_divisors = sum_of_divisors + i
    i += 1
if (sum_of_divisors == num):
    print(f"{num} is Perfect Number,")
else:
    print("Not perfect Number.")
