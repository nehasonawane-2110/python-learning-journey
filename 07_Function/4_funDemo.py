# Types of User-defined function
# 3) Function without argument and with return value.
# Example. - Factorial of Number

# Without passing paramenter (without I/P)
# with return value (With O/P)

def fact():
    num = int(input("Enter the Number: "))
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial    # when u can't return any value then it print None so for this user-defined fun its compulsory to return value


result = fact()   # Function called - stores the returned value
print("factorial is", result)
