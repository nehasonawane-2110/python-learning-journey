# Dictionary Methods 

employee = {"name": "Kunal Sonawane", "age": 24, "Address": "nashik", "Company": "Propix Pune", "Salary": 30000}

# 1) clear() - This method is used to remove all item from the dictionary.
# Example -
# employee.clear()
# print(employee)      # output - {} empty dictionary

# 2) copy() - This method is used to create a shallow copy of the dictionary, create a new dictionary with the same key-value pairs as the original dictionary.
# Example -
employee_data = employee.copy()
print(employee_data)  # output - {'name': 'Kunal Sonawane', 'age': 24, 'Address': 'nashik', 'Company': 'Propix Pune', 'Salary': 30000}

# 3) get() - Safely get value (no error if key not found
# example - 
print(employee.get('name', "Key not found"))  # output - Kunal Sonawane
print(employee.get('email', "Key not found")) # output - Key not found because email key is not present in dict

# 4) items() - This method is used to return a view object that displays a list of dictionary's key-value tuple pairs.
# example - 
print(employee.items())  # output - dict_items([('name', 'Kunal Sonawane'), ('age', 24), ('Address', 'nashik'), ('Company', 'Propix Pune'), ('Salary', 30000)])

# 5) keys() - Returns all keys
# example -
print(employee.keys())   # output - dict_keys(['name', 'age', 'Address', 'Company', 'Salary'])

# 6) values() - Returns all values
# example -
print(employee.values())  # output - dict_values(['Kunal Sonawane', 24, 'nashik', 'Propix Pune', 30000])

# 7) pop() - Removes element using key
# example -
employee.pop('age')
print(employee)  # output - {'name': 'Kunal Sonawane', 'Address': 'nashik', 'Company': 'Propix Pune

# 8) popitem() - Removes last inserted item
# example -
employee.popitem()
print(employee)

# 9) update() - Update or add multiple values 
# example -
employee.update({"age": 24, "email": "kunal@propix.com"})
print(employee)
