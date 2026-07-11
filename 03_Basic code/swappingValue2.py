# swapping values
# swap the value does not using third variable

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print(f'Before swapping: a={a}, b={b}.')

# logic 1
## a , b = b , a  # a = b, b = a

# Logic 2
a = a + b   # sum of a and b is stored in b
b = a - b   # original value of a is stored in b
a = a - b   # original value of b is stored in a


print(f'After swapping: a={a}, b={b}.')
