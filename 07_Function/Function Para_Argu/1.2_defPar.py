# Example 2- Default Parameter 

def greet(name, message='Good Morning'):
    return name, message


print(greet('Neha', 'Good Evening'))
print(greet('Kunal'))