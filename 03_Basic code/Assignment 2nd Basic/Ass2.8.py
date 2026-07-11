# Write a program to reverse three-digit number.
num = int(input("Enter the three digit number: "))
temp = num
digit1 = temp % 10
temp = temp // 10
digit2 = temp % 10
temp = temp // 10
digit3 = temp % 10
temp = temp // 10
reversed = (digit1 * 100) + (digit2 * 10) + digit3
print(f'Reversed number of {num} is : {reversed}')
