# Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter the three digit number: "))
original = num   # store the original number

# extract digits
last = num % 10
middle = (num // 10) % 10
first = num // 100

# reverse the number
reverse_num = (last * 100) + (middle * 10) + first

# check palindrome
if original == reverse_num:
    print("The number is a Palindrome")
else:
    print("The number is not a Palindrome")
