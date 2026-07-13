# 3) Variable number of arguments / Variable length Parameter.
# - A variable number of argument means a function can accept any number of argument.
# - In python this can done by using *
# Syntax
# def function_name(*parameter):
#   function body

# Example -
# 1. Mentioned asterisk(*) symbol before parameter in function defination.

def add(*data):
    print(type(data))   # types - tuple
    print(data)         # data print as it is in the function called multiple number can print by using this types. 


add(10, 20)
add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
