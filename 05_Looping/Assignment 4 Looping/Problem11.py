# Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)

num = int(input("Enter the number: "))
temp = num
count = 0     # count the number of digits in the given number.(153 has 3 digits)
while (temp > 0):
    temp = temp // 10
    count += 1
temp = num           # temp usde to stored the original number after the digit separate process.(153)
sum_of_power = 0      # strore the sum of digits power(1^3 + 5^3 + 3^3 = 153)
while (temp > 0):
    digit = temp % 10     # digit separate (153 % 10 = 3, 15 % 10 = 5, 1 % 10 = 1)
    sum_of_power = sum_of_power + digit ** count
    temp = temp // 10
if (sum_of_power == num):
    print(f'{num} is an Armstrong number.')
else:
    print(f'{num} is not an Armstrong number.')
