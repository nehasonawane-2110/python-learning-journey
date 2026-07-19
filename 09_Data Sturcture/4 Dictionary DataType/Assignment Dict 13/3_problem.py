# 3) Python Program to Check if a Given Key Exists in a Dictionary or Not

emp = {'name':'Kunal', 'age': 24, 'address': 'nashik', 'company': 'Propix pune'}
key = input('Enter key to check: ')
if key in emp:
    print(f'{key} is present in the dictionary.')
else:
    print(f'{key} is not present in the dictionary.')