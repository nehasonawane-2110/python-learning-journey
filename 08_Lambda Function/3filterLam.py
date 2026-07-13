# using lambda with filter function.

# fliter() keep only the elements that return True from a function.
# selsect only requied element based on condtions


# Example - filter out the even number from a list of numbers

numbers = [0, 34, 57, 84, 33, 92, 28, 65, 65, 77]
res = list(filter(lambda x: x % 2 == 0, numbers))
print(res)
