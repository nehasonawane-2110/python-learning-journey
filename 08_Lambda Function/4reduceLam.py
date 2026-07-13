# using lambda with reduce function.
# reduce() take a list and combines all elements step by step into one result
# it not built-in function we need to import it from functools module.

# syntax
# reduce(function, iterable) - function(parameter), iterable(list, tuple)

# example - sum of series of numbers

import functools      # import the reduce function from functools module

numbers = [0, 34, 57, 84, 33, 92, 28, 65, 65, 77]

result = functools.reduce(lambda x, y: x + y, numbers)
print(result)
