# Types of User-defined function
# 4) Function with argument and with return value.
# Example. - Prime Number 

# With passing paramenter (without I/P)
# with return value (With O/P)

def checkPrime(num):                        
    for i in range(2, num // 2 + 1):         # Loop from 2 to num/2 to check divisibility
        
        if (num % i == 0):                   # Check if number is divisible by i
            return False                     # If divisible → not a prime number
    
    else:                                    # If loop finishes without finding factor
        return True                          # Number is prime


num = int(input("Enter the Number: "))       # Taking number input from user

res = checkPrime(num)                        # Calling function and storing result

if (res):                                    
    print(f'{num} is a prime number.')       
else:                                       
    print(f'{num} is not a prime number.')   