# 7) Python Program to Remove the Given Key from a Dictionary

emp = {'name':'Kunal', 'age': 24, 'address': 'nashik', 'company': 'Propix pune'}
key = input('Enter key to remove: ')
if key in emp:
    emp.pop(key)  # pop() method will remove the key value pair from the dict and return the value of removed key
    print(f'{key} has been removed from the dictionary.')
else:
    print(f'{key} is not present in the dictionary.')
print("Updated dictionary:", emp)