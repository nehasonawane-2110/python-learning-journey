# write the program to calculate sum of all digite in three or four perform addition of tha number

num = int(input("Enter the 3 or 4 digit number: "))
temp = num
sum_digits = 0
while (temp > 0):
    d = temp % 10
    sum_digits = sum_digits + d
    temp = temp // 10
print("sum of digits is ", sum_digits)
