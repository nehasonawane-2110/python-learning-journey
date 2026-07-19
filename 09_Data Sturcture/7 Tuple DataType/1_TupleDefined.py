# Tuple Data type -
# - A tuple is an ordered and immutable collection of elements in python its used to store multiple value in single variable

# 1) sturcture -
# - a tuple is denoted by round brackets ()
# - one element need to use comma

tu = (10)
print(type(tu))  # int data type is provided so that why , comma operator used for singal ele defind
tu = (10,)  # single ele
print(tu)
print(type(tu))
tu = (10, 20, 30, 40, 50)
print(tu)

# 2) Type of data  ( heterogenous)
# - tuple can stored differet type of data
tu = (10, 20, 'a',3.16)
print(tu)

# 3) sequence (ordered)
# - each elements has fixed pointion(index)
# - elements can be accessed using indexing
tu = (10, 'abc', 0)
print(tu)
print([100])


# 4) chnagable ( immutable)
# - tuple are immutable their element cannot be chnage after creation
# t = (19, 20, 12, 13)
# t[1] = 50 # error


# 5) faster then list 
# - tuple allowed duplicated value 
# - the same value can apperr more than one
