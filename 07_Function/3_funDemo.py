# Types of User-defined function
# 2) Function with argument and without return value.
# Example. - Addtion of two number

# With passing paramenter (with I/P)
# without return value (Without O/P)

def Addtion(Num1, Num2):    # Num1, Num2 is an formal Parameter or argument
    print(f'Addtion Of {Num1} and {Num2} is {Num1 + Num2}.')


X = int(input("Enter the Number 1: "))
Y = int(input("Enter the Number 2: "))

Addtion(X, Y)   # X, Y is Actual Paramenetr or argument

# positional Parameter (X, Y) = The sequence of passing paramertes is important.
