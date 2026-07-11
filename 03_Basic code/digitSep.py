# Digit Seperator

num = int(input("Enter the three digit number: "))
temp = num    # storing the value of num in temp variable
digit1 = temp % 10    # extracting the last digit  (258 % 10 = 8)
temp = temp // 10     # removing the last digit from temp (258 // 10 = 25)

digit2 = temp % 10     # extracting the second last digit (25 % 10 = 5)
temp = temp // 10      # removing the second last digit from temp (25 // 10 = 2)

digit3 = temp % 10      # extracting the first digit (2 % 10 = 2)
temp = temp // 10       # removing the first digit from temp (2 // 10 = 0)


print(f'd1: {digit1}, d2: {digit2}, d3: {digit3}.')
