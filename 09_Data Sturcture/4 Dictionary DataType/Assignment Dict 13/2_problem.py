# 2)Python Program to Concatenate Two Dictionaries Into One

book1 = {'name': 'python', 'author': 'xyz', 'price': 500}
book2 = {'name': 'java', 'author': 'abx', 'price': 200}
book3 = {**book1, **book2}   # unpacking both dict and creating new dict
print(book3)