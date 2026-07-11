# Identity Operaters
# used to compare memory location of object.

x = 10
y = 20
z = 10

# 1 is
# True if both refer to same object
print(x is y)
print(x is z)



li1 = [10, 20, 30]
li2 = [10, 20, 30]
print(li1 is li2)  # output while be false because memory address is not same
# of li1 and li2 that why its print false.
print("id of li1 and li2:")
print(id(li1))
print(id(li2))



# print id of x and y.
print("id of x and z: ")
print(id(x))
print(id(z))
# print same id that why output of x is z is true. not false.
