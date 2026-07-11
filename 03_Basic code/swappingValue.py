# Swapping values
# swap the value of two variables to each other swap, using third variable

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
z = 0  # storing temporary value

z = x    # storing the value of x in z
x = y    # storing the value of y in x
y = z     # storing the value of z in y

print(f'After swapping, value of x: {x}, value of y: {y}.')
