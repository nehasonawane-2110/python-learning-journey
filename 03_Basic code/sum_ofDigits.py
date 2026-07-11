# sum of digit of a three digit number

num = int(input("Enter the three digit number: "))
temp = num
sum_of_digits = 0

digit1 = temp % 10
temp = temp // 10
sum_of_digits = sum_of_digits + digit1

digit2 = temp % 10
temp = temp // 10
sum_of_digits = sum_of_digits + digit2

digit3 = temp % 10
temp = temp // 10
sum_of_digits = sum_of_digits + digit3

print(f'The sum of digits of {num} is {sum_of_digits}.')
