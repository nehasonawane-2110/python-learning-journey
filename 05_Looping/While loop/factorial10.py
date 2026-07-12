# factorial program

num = 5          # number whose factorial we want to calculate
i = 1            # loop counter starts from 1
fact = 1         # stores the factorial result (initialized to 1)

while i <= num:  # loop runs until i becomes greater than num
    fact = fact * i   # multiply current value of fact with i
    i += 1            # increase i by 1 in each iteration

print(f'Factorial of {num} is: {fact}.')
# f-string is used to insert variable values directly inside the string