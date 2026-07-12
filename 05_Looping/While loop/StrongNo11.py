# Strong number
# A number whose sum of the factorial of its digits it equal to the number itself is called a strong number.
# For example, 145 is a strong number because 1! + 4! + 5! = 145.

num = 145
temp = num
sum_of_digit = 0

while (temp > 0):
    digit = temp % 10
    temp = temp // 10


    fact = 1
    i = 1
    while (i <= digit):
        fact = fact * i
        i += 1

    sum_of_digit = sum_of_digit + fact
if (sum_of_digit == num):
    print(f'{num} is strong number.')
else:
    print(f'{num} is not strong number.')
