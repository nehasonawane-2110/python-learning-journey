# using lambda with map function.

# map function is a built-in function that applies a function to each item of a list (or iterable)
# map() is a function we can pass multiple inputs and get multiple outputs.
# when we used lambda , we don't need to define a separate function for map function we can directly use lambda function inside the map function.

# example - cube root of a list of number using a lambda function with map function.

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # lis of numbers

result = list(map(lambda num: num ** 3, data)) 
# lambda num: num ** 3 - this lambda function this function return cube of each number. 
# map() applies the lambda function to each element of data . But map() does NOT return a list, It returns a map object (iterator)
# list(...) Converts the map object into a list.
print(result)
