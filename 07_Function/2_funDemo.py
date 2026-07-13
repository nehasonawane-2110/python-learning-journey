# Types of User-defined function
# 1) Function without argument and without return value.
# Example. - Even/ odd Numbers

def evenOdd():          # Function Defined

    num = int(input("Enter the number to check number is even or odd: "))  # Body
    if (num == 0):
        print("Number is an Neutral.")
    elif (num % 2 == 0):
        print(f'{num} is an Even number.')
    else:
        print(f'{num} is an odd number.')


evenOdd()       # function call


# Why this is Function without argument and without return value

# No Argument -	 evenOdd() does not take parameters
# No Return   -	 Function only prints result, no return used
# A function without argument and without return value is a function that does not accept parameters and does not return any value;
# it only performs a task when called.
