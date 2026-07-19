# 6) Python Program to Multiply All the Items in a Dictionary

dict = {'a': 100, 'b': 1000, 'c': 10000}
result = 1
for i in dict.values():   # iterate through all values in the dict
    result *= i     # multiply each value in the dict with result and update result
print("Multiplication of all item in the dictionary is:", result)
