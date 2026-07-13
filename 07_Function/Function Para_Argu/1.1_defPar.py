# Types Of function parameter / Argument.
# 1. Default Parameter.
# - A default Parameter is a parameter that already has a default value in the function definition. if the use does not pass a value python use the default value.

# Example 1
# 1. Assigning value to the parameter / argument in the function defintion
# 2. Flow should be right to left 
# 3. Invoking optional paramter concept.

def addtion(num1, num2, num3=0, num4=0):  # function def
    return num1 + num2 + num3 + num4


print(addtion(10, 20, 30, 40))  # function call first priority by default assign value not consider.
print(addtion(20, 30))
