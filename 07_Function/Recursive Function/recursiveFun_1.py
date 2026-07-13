###### Recursive Function #######
# Definition - A Recursive function is a function that calls irself to solve a problem.
# - It keeps calling itself with a smaller or simpler input until a stopping condtion (base case) is reached.

# Two types of Recursive Function -


##### 1). Direct Recursive function. #####
# - A Direct recursive function is a function that calls itself directly inside it own body.
# Syntax -
# def fun():
#   body_______
#   ___________
#   fun()
# fun()


##### 2) Indirect Recursive function. #####
# - An indircet Recursive function happens when one function call another function and that function class the first function again.
# - so Recursive happen between tow or more function.
# Syntax -
def functionA(parameters):
    # some statements
    functionB(parameters)   # calling another function


def functionB(parameters):
    # some statements
    functionA(parameters)   # calling first function again


# Example- 1
# Sum of series using Direct Recursive function.
# Function to calculate Sum Of Series (1 + 2 + 3 + ... + n) using recursion


def SOS(n):           # Define a function named SOS with parameter n
    if (n == 0):         # Base condition: if n becomes 0
        return 0         # Stop recursion and return 0
    else:                # If n is not 0
        return n + SOS(n-1)          # Add current n with recursive call of SOS(n-1)


n = int(input("Enter the Number: "))
sum = SOS(n)            # Call SOS function and store result in sum variable
print(sum)
