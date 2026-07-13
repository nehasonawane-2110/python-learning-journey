# Lambda Function
# A Lambda function in the python is a small anonymous (unnamed) function that is defined using the keyword lambda.

# syntax
# lambda parameter: expression
# 1- it can take any number of parameters
# 2- it  can have only one expression
# 3 - it return the result automatically (without using return keyword)

# example
# Addition of two numbers using lambda function.

add = lambda N1, N2: N1 + N2   # take a variable (add) then assign the lambda function to it. (N1, N2) are parameters and N1, N2 are the expression which is addition of two numbers.
result = add(10, 20)      # fuction call with parameters (10, 20) and store the result in variable (result)
print(result)         # print the result o/p = 30


# define one time and call multiple time.
