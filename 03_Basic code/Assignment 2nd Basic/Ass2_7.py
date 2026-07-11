# Find the sum of three-digit number.
num = int(input("Enter the three digit number: "))
temp = num
digit1 = temp % 10
temp = temp // 10
digit2 = temp % 10
temp = temp // 10
digit3 = temp % 10
temp = temp // 10
sumDigits = digit1 + digit2 + digit3
print(f'Sum of digits in {num} is : {sumDigits}')
